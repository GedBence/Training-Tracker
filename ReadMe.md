# 🥊 Training Tracker

Python alapú, magyar nyelvű edzéskövető és edzésterv-generáló alkalmazás több sportághoz.

Rögzítsd az edzéseidet, gyűjtsd a saját gyakorlataidat, és kövesd az edzésidődet és az intenzitásodat. Ha ötletre van szükséged, a program véletlenszerű edzéstervet is összeállít a választott sportág gyakorlataiból.

> Verzió: v0.3.1 – helyi hibajavításokkal
>
> Állapot: 🚧 Fejlesztés alatt
>
> Felület: magyar nyelvű, terminálban használható menü

---

## 🎯 Projekt célja

A projekt célja egy egyszerűen használható edzésnapló készítése, amelyben többféle sportág edzései egy helyen követhetők.

A program segítségével:

- új edzéseket rögzíthetsz;
- gyakorlatokat és sportágspecifikus adatokat adhatsz az edzésekhez;
- megtekintheted, szerkesztheted és törölheted a korábbi edzéseidet;
- összesített statisztikát kaphatsz az edzéseidről;
- saját fókuszokat és gyakorlatokat vehetsz fel;
- véletlenszerű edzéstervet generálhatsz.

---

## ⚙️ Jelenlegi funkciók

### 🥊 Edzés rögzítése

Minden edzéshez megadható:

- **dátum:** `ÉÉÉÉ.HH.NN`, például `2026.11.11`;
- **sportág:** választás a meglévő listából vagy új sportág felvétele;
- **időtartam:** pozitív egész szám, percben;
- **fókusz:** meglévő fókusz kiválasztása vagy saját fókusz megadása;
- **intenzitás:** egész szám 1 és 10 között;
- **gyakorlatok:** tetszőleges számú, szövegesen megadott gyakorlat.

A beépített sportágakhoz külön adatok is rögzíthetők:

| Sportág | Rögzíthető egyedi adatok |
| --- | --- |
| Muay Thai | Volt-e sparring, menetek száma |
| Box | Menetek és KO-k száma |
| Futás | Távolság kilométerben, átlagtempó perc/km formában |
| Úszás | Távolság méterben, úszásstílus |
| Erősítő edzés | Fő izomcsoport, szettek száma |
| Kerékpározás | Távolság kilométerben, átlagsebesség km/h-ban |

A számmal megadott egyedi adatok nem lehetnek negatívak. Tizedes értékeknél pontot és vesszőt is használhatsz, például `5.5` vagy `5,5`.

### 📋 Edzések megtekintése és kezelése

A mentett edzések sorszámozott listában jelennek meg, az alapadatokkal, az egyedi adatokkal és a gyakorlatokkal együtt.

Szerkesztéskor az **ENTER** megtartja az adott mező korábbi értékét. A sportág is megváltoztatható: ilyenkor a régi sportághoz tartozó egyedi adatok törlődnek, és új fókuszt kell választani. A meglévő gyakorlatok megmaradnak; külön szerkesztésük jelenleg nem támogatott.

Törlés előtt a program megerősítést kér.

### 📊 Statisztikák

A program az alábbi összesítéseket jeleníti meg:

- edzések száma;
- összes edzésidő percben;
- átlagos intenzitás az 1–10-es skálán;
- edzések száma sportáganként.

### 🎲 Véletlenszerű edzésterv-generátor

A generátor a kiválasztott beépített sportág gyakorlataiból állít össze tervet. A választható fókuszok sportáganként eltérnek: például technika, védekezés, erőnlét, intervallum vagy állóképesség.

- **Egy fókusz kiválasztásakor:** legfeljebb három különböző gyakorlatot választ.
- **Random módban:** minden elérhető, nem üres fókuszból egy gyakorlatot választ.
- A saját, elmentett gyakorlatokat is felhasználja.
- A tervhez 10 perc bemelegítést és 5 perc levezetést jelez.

A generált terv a képernyőn jelenik meg; nem kerül automatikusan az edzésnaplóba.

### ➕ Saját gyakorlatok és sportágak

Az edzés rögzítésekor megadott új gyakorlat a kiválasztott sportághoz és fókuszhoz is elmentődik. Az ugyanilyen sportág–fókusz pároshoz már felvett, pontosan azonos szövegű gyakorlatot nem menti el újra.

Új sportág is felvehető. Ha tartozik hozzá mentett edzés, újraindítás után is megjelenik az edzésrögzítés sportlistájában.

---

## 🚀 Telepítés és indítás

### 1. Python telepítése

A futtatáshoz Python 3 szükséges. Külön Python-csomagokat nem kell telepíteni: a projekt a Python beépített eszközeit használja.

### 2. Projekt letöltése

A GitHubon válaszd a **Code → Download ZIP** lehetőséget, majd csomagold ki a letöltött fájlt.

Ha már telepítetted a Gitet, a projektet ezzel a paranccsal is letöltheted:

```bash
git clone https://github.com/GedBence/Training-Tracker.git
cd Training-Tracker
```

### 3. Program indítása

Nyiss terminált abban a mappában, ahol a `main.py` fájl található, majd Windowson futtasd:

```powershell
py main.py
```

Más rendszeren, vagy ha a gépeden más néven érhető el a Python:

```bash
python main.py
```

Szükség esetén a `python3 main.py` parancsot használd.

### 4. Menü használata

Írd be a kívánt menüpont számát, majd nyomj ENTER-t:

```text
1. Új edzés
2. Edzések megtekintése
3. Statisztikák
4. Random edzés
5. Edzés szerkesztése
6. Edzés törlése
0. Kilépés
```

---

## 💾 Adatok tárolása

A program JSON-fájlokat használ. A JSON egy szöveges adatformátum, amelyben az edzések és a gyakorlatok strukturáltan tárolhatók.

| Fájl | Tartalom |
| --- | --- |
| `training.json` | Mentett edzések; az első sikeres mentéskor jön létre |
| `data/costum_exercises.json` | Saját gyakorlatok sportág és fókusz szerint |

Az útvonalak a projekt mappájához kötöttek, ezért a mentések helye nem függ a terminál aktuális munkamappájától.

Mentéskor először egy ideiglenes fájl készül. A program csak sikeres írás után cseréli le a korábbi adatfájlt. Ettől függetlenül a fontos adataidról érdemes külön biztonsági másolatot készíteni.

Hibás JSON-szintaxis esetén a betöltés hibaüzenetet ad, és nem helyettesíti automatikusan üres adatokkal a sérült fájlt. Az edzésfájl ilyen hibája az indulást is megakadályozza. Visszaállítás előtt készíts másolatot az érintett fájlról.

---

## 🗂️ Projektstruktúra

```text
Training-Tracker/
├── main.py                      # A program indítása és a menüpontok kezelése
├── models/
│   ├── __init__.py
│   ├── training.py              # Egy edzés adatai és megjelenítése
│   └── sport.py                 # Egy sportág adatai
├── services/
│   ├── __init__.py
│   ├── generator.py             # Edzésterv-generálás és fókuszválasztás
│   ├── storage.py               # Edzések betöltése és mentése
│   └── exercise_storage.py      # Saját gyakorlatok kezelése
├── data/
│   ├── exercises.py             # Beépített gyakorlatok
│   ├── sports.py                # Sportágak és egyedi kérdések
│   └── costum_exercises.json    # Saját gyakorlatok adatfájlja
├── utils/
│   ├── __init__.py
│   └── menu.py                  # A főmenü megjelenítése
├── tests/
│   └── test_regressions.py      # Automatikus ellenőrzések
└── ReadMe.md
```

A futás közben létrejövő `training.json` a `main.py` mellett található. A `costum_exercises.json` fájlnév a projekt jelenlegi elnevezését követi.

---

## 🧪 Automatikus ellenőrzések

A projekt főmappájából futtasd:

```powershell
py -B -m unittest discover -s tests -v
```

Ha a gépeden a `python` vagy a `python3` parancs érhető el, a `py` helyett azt használd.

A tesztek ellenőrzik a mentést és visszatöltést, a korábbi mentés megőrzését sikertelen adatátalakítás esetén, a saját gyakorlatokat, a generátort, a hibás számbemenetet, a sérült edzésfájlt, a szerkesztést és a sportágankénti összesítést.

A tesztek ideiglenes mappában dolgoznak, a saját edzésadataidat nem módosítják.

---

## 🔧 A helyi változat hibajavításai

- A mentés a sport nevét tárolja a teljes Python-objektum helyett.
- Javítva a saját gyakorlat hozzáadása és az ismétlődések ellenőrzése.
- Megjelennek a sportághoz tartozó fókuszok és egyedi kérdések.
- Az edzésszerkesztés már nem hivatkozik nem létező mezőre.
- A statisztika név szerint összesíti az azonos sportágakat.
- A generátor a saját gyakorlatokat is felhasználja.
- A számos egyedi adatoknál a program elutasítja a hibás, negatív és nem véges értékeket.
- A mentési útvonalak a projekt mappájához kötődnek.
- Javítva néhány felirati elírás és a dokumentáció szerkezete.

---

## 🚧 Jelenlegi korlátok és lehetséges fejlesztések

A program jelenleg terminálban használható. Asztali grafikus felület és SQL-adatbázis még nincs benne.

További korlátok:

- A generátor sportválasztója csak a beépített sportágakat kínálja fel.
- A mentett edzés nélküli saját sportág nem marad meg újraindítás után.
- A kézzel módosított adatfájlok teljes tartalmi ellenőrzése még nem megoldott.
- A szöveges mezők, például az átlagtempó formátumát a program nem ellenőrzi teljeskörűen.

Lehetséges következő fejlesztések:

- SQLite-adatbázis az adatok tárolásához;
- asztali felület ablakokkal, gombokkal és űrlapokkal;
- edzések keresése és szűrése dátum vagy sportág szerint;
- heti célok és részletesebb statisztikák;
- generált edzéstervek mentése.
