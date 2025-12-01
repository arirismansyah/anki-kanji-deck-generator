# Anki Kanji Deck Generator

A Python package designed to **generate Anki flashcard decks for JLPT and Kyōiku Kanji with highly customizable templates**. This tool provides a clean API using the `KanjiDeck` class to fetch comprehensive data from the **Kanjilive API** and build structured Anki decks (.apkg files) using the **genanki** library.

## 🌟 Features

* **Flexible API:** Easy-to-use `KanjiDeck().generate_deck()` method allows simple deck creation via code.
* **Dual Filtering Support:** Generate decks based on:
    * **JLPT Levels:** N5, N4, N3, N2, N1.
    * **Kyōiku Grades:** Grade 1 through Grade 6.
* **Customizable Templates:** Supports using custom HTML and CSS templates for unique card styling.
* **Simple Installation:** Available directly via PyPI.

---

## 🛠️ Prerequisites

* **Python 3.11** or newer.

---

## 🚀 Installation

Install the package directly from PyPI using pip:

```bash
pip install anki-kanji-deck-generator
````

-----

## 💡 Usage

The primary way to use this tool is by importing the `KanjiDeck` class and calling the `generate_deck` method with the desired parameters within a Python script.

### Example: Generating All Decks

Create a Python file (e.g., `generate_all.py`) and include the following code to generate all JLPT and Kyōiku Grade decks:

```python
from kanjideck_generator import KanjiDeck
# Initialize the deck generator
generator = KanjiDeck()

# --- Generate JLPT Decks (N5 to N1) ---
print("Generating JLPT decks...")
generator.generate_deck(level_type='jlpt', level='n5', output_filename='jlpt_n5_deck.apkg')
generator.generate_deck(level_type='jlpt', level='n4', output_filename='jlpt_n4_deck.apkg')
generator.generate_deck(level_type='jlpt', level='n3', output_filename='jlpt_n3_deck.apkg')
generator.generate_deck(level_type='jlpt', level='n2', output_filename='jlpt_n2_deck.apkg')
generator.generate_deck(level_type='jlpt', level='n1', output_filename='jlpt_n1_deck.apkg')

# --- Generate Kyōiku Grade Decks (Grade 1 to 6) ---
print("Generating Grade decks...")
generator.generate_deck(level_type='grade', level=1, output_filename='grade_1_deck.apkg')
generator.generate_deck(level_type='grade', level=2, output_filename='grade_2_deck.apkg')
generator.generate_deck(level_type='grade', level=3, output_filename='grade_3_deck.apkg')
generator.generate_deck(level_type='grade', level=4, output_filename='grade_4_deck.apkg')
generator.generate_deck(level_type='grade', level=5, output_filename='grade_5_deck.apkg')
generator.generate_deck(level_type='grade', level=6, output_filename='grade_6_deck.apkg')
```
```


### Running the Example

Execute the script using your Python interpreter:

```bash
python generate_all.py
```

### Importing into Anki

Find the generated `.apkg` files in the directory where you ran the script, open your Anki application, and import them via **File** → **Import**.

-----

## 📸 Screenshots

Here are examples of the generated Anki flashcards as they appear in the AnkiDroid mobile app:

### Front of the Card
The front of the card typically displays the Kanji character, prompting the user to recall its meaning and readings.

### Back of the Card
The back of the card reveals all about the Kanji including readings, meanings, and mnemonic hint.

<img src="https://github.com/arirismansyah/anki-kanji-deck-generator/blob/master/src/kanjideck_generator/media/front.jpeg" height='500px'>
<img src="https://github.com/arirismansyah/anki-kanji-deck-generator/blob/master/src/kanjideck_generator/media/back.jpeg" height='500px'>



## 📦 Key Dependencies

This package automatically installs the following core dependencies:

  * `genanki`: For programmatic generation of Anki decks.
  * `requests`: For fetching data from the Kanjilive API.
  * `pandas`: For data manipulation and structuring.
  * `pydantic`: For validating the fetched Kanji data schema.

-----

## 🤝 Credits

This project relies on the following excellent tools and services:

  * **[Kanjilive API](https://www.google.com/search?q=https://kanjilive.com/)**: The source for comprehensive Kanji data.
  * **[genanki](https://github.com/kerrickstaley/genanki)**: The library used for deck construction.

## 📄 License

This project is licensed under the **MIT License**.
