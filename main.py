# Komentarz
import json

print("Git handson")

DATA = [
    {
        "imię": "Filemon",
        "gatunek": "Kot",
        "waga": 1,
        "wiek": 0.5
    },
    {
        "imię": "Szarik",
        "gatunek": "Pies",
        "waga": 30,
        "wiek": 2
    }
]

def Display(dane):
    print(dane)

f = open("data.json")
D = json.load(f)
Display(D)