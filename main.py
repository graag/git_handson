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

f2 = open("data2.json")
D2 = json.load(f2)

D.extend(D2)

Display(D)