
# Periodic Information Finder
from pyscript import display
from pyscript import document

non_metals = {
    "H":  {"name": "Hydrogen",   "number": 1,  "mass": 1.008},
    "He": {"name": "Helium",     "number": 2,  "mass": 4.003},
    "C":  {"name": "Carbon",     "number": 6,  "mass": 12.011},
    "N":  {"name": "Nitrogen",   "number": 7,  "mass": 14.007},
    "O":  {"name": "Oxygen",     "number": 8,  "mass": 15.999},
    "F":  {"name": "Fluorine",   "number": 9,  "mass": 18.998},
    "Ne": {"name": "Neon",       "number": 10, "mass": 20.180},
    "P":  {"name": "Phosphorus", "number": 15, "mass": 30.974},
    "S":  {"name": "Sulfur",     "number": 16, "mass": 32.06},
    "Cl": {"name": "Chlorine",   "number": 17, "mass": 35.45},
    "Ar": {"name": "Argon",      "number": 18, "mass": 39.948},
    "Se": {"name": "Selenium",   "number": 34, "mass": 78.971},
    "Br": {"name": "Bromine",    "number": 35, "mass": 79.904},
    "Kr": {"name": "Krypton",    "number": 36, "mass": 83.798},
    "I":  {"name": "Iodine",     "number": 53, "mass": 126.904},
    "Xe": {"name": "Xenon",      "number": 54, "mass": 131.293},
    "Rn": {"name": "Radon",      "number": 86, "mass": 222},
}

result_box = document.getElementById("result")

def search_element(event):

    symbol = document.getElementById("symbol_input").value.strip().capitalize()

    try:
        element = non_metals[symbol]

        result_box.innerText = (
            f"Symbol: {symbol}\n"
            f"Element: {element['name']}\n"
            f"Atomic Number: {element['number']}\n"
            f"Atomic Mass: {element['mass']}"
        )

    except KeyError:
        result_box.innerText = (
            f"Sorry, '{symbol}' does not exist in the non-metals list."
        )
