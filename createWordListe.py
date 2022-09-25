import json, os, unidecode

jsonWordListe = {
    "a": [],
    "b": [],
    "c": [],
    "d": [],
    "e": [],
    "f": [],
    "g": [],
    "h": [],
    "i": [],
    "j": [],
    "k": [],
    "l": [],
    "m": [],
    "n": [],
    "o": [],
    "p": [],
    "q": [],
    "r": [],
    "s": [],
    "t": [],
    "u": [],
    "v": [],
    "w": [],
    "x": [],
    "y": [],
    "z": []
}

if os.path.exists("liste_francais.txt"):
    with open("liste_francais.txt", "r", encoding='utf-8') as file:
        for mot in file:
            mot = mot.split("\n")[0]
            startLetter = unidecode.unidecode(mot[0]).lower()
            jsonWordListe[startLetter].append(mot)

else:
    print("error word list not exist")
    
with open("liste_francais.json", "w+", encoding='utf8') as file:
    json.dump(jsonWordListe, file, indent = 4, ensure_ascii=False)