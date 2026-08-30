# 🥊Training Tracker

Egy Python alapú edzéskövető és edzésterv-generáló alkalmazás többféle edzéstípushoz.

A projekt célja egy olyan alkalmazás készítése, amely segítségével nyomon követhetők az edzések, a gyakorlatok és az edzésintenzitás, valamint automatikusan generálható egy véletlenszerű edzésterv, abban a sportágban, amit szeretnénk(és ami adott jelenleg).

> Current version: v0.3.0
> Status: 🚧 In development

---

## 🎯 Projekt célja

A program segítségével a felhasználó:

- új, több sporthoz való edzéseket rögzíthet
- gyakorlatokat adhat az edzésekhez
- megtekintheti korábbi edzéseit
- statisztikákat kaphat az edzéseiről
- véletlenszerű edzéstervet generálhat
- módosíthatja az eddigi edzéseit utólag
- törölhet edzést

---

## ⚙️ Jelenlegi funkciók

### 🥊 Edzés rögzítése

Az edzéshez megadható:

- dátum
- edzés típusa
- időtartam
- edzés fókusza
- intenzitás (1–10)
- gyakorlatok

Specifikus kérdésekre is adhatunk választ:
- küzdősportál volt-e sparring, ha igen hány menet volt
- futásnál hány km-t futottunk és milyen volt az átlagtempó
- úszásnál milyen távot úsztunk és az úszás stílusa
- erősítő edzésnél az izomcsoportot és a szetteket tudjuk megadni
- kerékpározásnál szintén a távolságot és az átlagsebességet (km/h)

### 📋 Edzések megtekintése

A program megjeleníti a korábban létrehozott edzéseket és azok adatait.

### 📊 Statisztikák

A program jelenleg az alábbi adatokat számolja:

- összes edzés
- összes edzésidő
- átlagos edzésintenzitás

### 🎲 Random edzésterv-generátor

A program véletlenszerűen állít össze edzéseket különböző fókuszok alapján a kért sportban:

- Technika
- Védekezés
- Erőnlét
- Intervallum
- Erősítő edzéshez setteket
- Állóképesség
- Random

---

## 🗂️ Projektstruktúra

```text
Training_tracker/
│
├── main.py
│
├── models/
│   ├── __init__.py
│   └── training.py
│
├── services/
│   ├── __init__.py
│   └── generator.py
│   └── storage.py
│
├── data/
│   └── exercises.py
│   └── sport.py
│
├── utils/
│   ├── __init__.py
│   └── menu.py
│
└── README.md