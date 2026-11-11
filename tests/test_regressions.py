import contextlib
import io
import json
from pathlib import Path
import runpy
import tempfile
import unittest
from unittest.mock import patch

from models.sport import Sport
from models.training import Training
from services import storage, exercise_storage, generator
from data.sports import ask_sport_details


class RegressionTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.path = Path(self.directory.name)
        self.enterContext(patch.object(storage, 'FILE_NAME', self.path / 'training.json'))
        self.enterContext(patch.object(exercise_storage, 'FILE_PATH', self.path / 'custom.json'))
        self.enterContext(contextlib.redirect_stdout(io.StringIO()))

    def training(self):
        return Training('2026.11.11', Sport('Muay Thai'), 60, 'Technika', 5)

    def test_save_and_reload(self):
        training = self.training()
        training.add_exercise('Teszt')
        storage.save_trainings([training])
        loaded = storage.load_trainings()[0]
        self.assertEqual(str(loaded.sport), 'Muay Thai')
        self.assertEqual(loaded.exercises, ['Teszt'])

    def test_failed_serialization_preserves_existing_file(self):
        storage.save_trainings([self.training()])
        before = storage.FILE_NAME.read_bytes()
        training = self.training()
        training.details = {'invalid': object()}
        with self.assertRaises(TypeError):
            storage.save_trainings([training])
        self.assertEqual(storage.FILE_NAME.read_bytes(), before)

    def test_custom_exercise_and_generator(self):
        sport = Sport('Muay Thai')
        self.assertTrue(exercise_storage.add_custom_exercise(sport, 'Sajat', 'Teszt'))
        self.assertFalse(exercise_storage.add_custom_exercise(sport, 'Sajat', 'Teszt'))
        self.assertEqual(generator.get_exercise_pools(sport)['Sajat'], ['Teszt'])
        output = io.StringIO()
        with patch('builtins.input', side_effect=['1', '4']), contextlib.redirect_stdout(output):
            generator.generate_training_plan()
        self.assertIn('Teszt', output.getvalue())

    def test_invalid_numeric_input_is_retried(self):
        with patch('builtins.input', side_effect=['bad', '-1', '3', '0']):
            self.assertEqual(ask_sport_details(Sport('Box')), {'menetek': 3, 'ko': 0})

    def test_corrupt_file_is_preserved(self):
        storage.FILE_NAME.write_text('{broken', encoding='utf-8')
        with self.assertRaises(ValueError):
            storage.load_trainings()
        self.assertEqual(storage.FILE_NAME.read_text(encoding='utf-8'), '{broken')

    def test_edit_statistics_and_custom_sport_reload(self):
        trainings = [self.training(), self.training(), Training('2026.11.11', Sport('Yoga'), 30, 'Relax', 2)]
        storage.save_trainings(trainings)
        with patch('builtins.input', return_value='0'):
            main = runpy.run_path(str(Path(__file__).resolve().parents[1] / 'main.py'))
        self.assertIn('Yoga', [str(s) for s in main['sports']])
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            main['show_statistics']()
        self.assertIn('Muay Thai: 2 db', output.getvalue())
        with patch('builtins.input', side_effect=['1', '', '', '', '', '', '', '']):
            main['edit_training']()
        self.assertEqual(len(storage.load_trainings()), 3)


if __name__ == '__main__':
    unittest.main()
