# Welcome to Interactive Constellation Map

```
          ╦ ╦╔═╗╦  ╔═╗╔═╗╔╦╗╔═╗  ╔╦╗╔═╗
          ║║║║╣ ║  ║  ║ ║║║║║╣    ║ ║ ║
          ╚╩╝╚═╝╩═╝╚═╝╚═╝╩ ╩╚═╝   ╩ ╚═╝
     ╔═╗╔═╗╔╗╔╔═╗╔╦╗╔═╗╦  ╦  ╔═╗╔╦╗╦╔═╗╔╗╔  ╔╦╗╔═╗╔═╗
     ║  ║ ║║║║╚═╗ ║ ║╣ ║  ║  ╠═╣ ║ ║║ ║║║║  ║║║╠═╣╠═╝
     ╚═╝╚═╝╝╚╝╚═╝ ╩ ╚═╝╩═╝╩═╝╩ ╩ ╩ ╩╚═╝╝╚╝  ╩ ╩╩ ╩╩
```

An interactive Python application for exploring constellations, learning star coordinates, and testing your astronomy knowledge.

---

## Features

- **2D Star Map** — A Matplotlib-rendered sky chart plotting 60+ named stars by Right Ascension and Declination, with constellation lines drawn for major groups.
- **Constellation Explorer** — Select any constellation to see an interactive Plotly chart zoomed into that group, complete with star labels, hover details, and a printed info card (alias, major stars, fun fact).
- **Constellation Quiz** — A 10-question Tkinter GUI quiz covering constellation mythology, shapes, and notable stars — with instant feedback and a final score.

---

## Constellations Included

| Constellation | Key Stars |
|---|---|
| Orion | Betelgeuse, Rigel, Bellatrix, Mintaka, Alnilam, Alnitak, Saiph |
| Ursa Major | Dubhe, Merak, Phecda, Megrez, Alioth, Mizar, Alkaid |
| Ursa Minor | Polaris, Kochab, Pherkad, Yildun |
| Cassiopeia | Schedar, Caph, Gamma Cas, Ruchbah, Segin |
| Leo | Regulus, Denebola, Algieba, Zosma, Chort |
| Taurus | Aldebaran, Elnath, Pleione |
| Gemini | Pollux, Castor, Wasat, Alhena |
| Scorpius | Antares, Dschubba, Shaula, Sargas |
| Cygnus | Deneb, Sadr, Albireo, Gienah |
| Lyra | Vega, Sheliak, Sulafat |

---

## Project Structure

```
constellation-map/
│
├── main.py                   # Main program — menu loop and all core functions
├── constellation_data.txt    # Constellation info file (alias, major stars, facts)
├── requirements.txt          # Python dependencies
└── README.md
```

### `constellation_data.txt` format

The info file is parsed by `load_constellation_info()` and must follow this format:

```
[Orion]
Alias: The Hunter
Major Stars: Betelgeuse, Rigel, Bellatrix, Mintaka
Fact: Orion is one of the most recognizable constellations in the night sky.

[Ursa Major]
Alias: The Great Bear
Major Stars: Dubhe, Merak, Alioth, Mizar, Alkaid
Fact: The Big Dipper is an asterism within Ursa Major.
```

---

## Requirements

- Python 3.8+
- matplotlib
- plotly
- adjustText
- tkinter *(included in most standard Python installations)*

Install dependencies:

```bash
pip install matplotlib plotly adjustText
```

---

## Usage

```bash
python main.py
```

You'll be presented with a menu:

```
Pick one to continue:
1. Basic 2D star map.
2. Know about major constellations.
3. Test your knowledge on constellations.
4. Exit
```

- **Option 1** — Opens a full-sky 2D star map with all plotted stars and constellation lines.
- **Option 2** — Lists available constellations and prompts you to pick one for a detailed interactive view.
- **Option 3** — Launches the 10-question GUI quiz.
- **Option 4** — Exits the program.

---
