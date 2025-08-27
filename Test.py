import json
import os

DATEI = "passwoerter.json"


def lade_passwoerter():
    if os.path.exists(DATEI):
        with open(DATEI, "r") as f:
            return json.load(f)
    return {}


def speichere_passwoerter(passwoerter):
    with open(DATEI, "w") as f:
        json.dump(passwoerter, f, indent=4)


def passwort_hinzufuegen():
    service = input("Name des Dienstes: ")
    benutzer = input("Benutzername: ")
    passwort = input("Passwort: ")
    
    passwoerter[service] = {"benutzer": benutzer, "passwort": passwort}
    speichere_passwoerter(passwoerter)
    print(f"Passwort für {service} gespeichert!")


def passwort_abrufen():
    service = input("Für welchen Dienst? ")
    if service in passwoerter:
        print(f"Benutzer: {passwoerter[service]['benutzer']}")
        print(f"Passwort: {passwoerter[service]['passwort']}")
    else:
        print("Dienst nicht gefunden.")


def passwort_loeschen():
    service = input("Welches Passwort löschen? ")
    if service in passwoerter:
        del passwoerter[service]
        speichere_passwoerter(passwoerter)
        print(f"{service} gelöscht!")
    else:
        print("Dienst nicht gefunden.")


passwoerter = lade_passwoerter()
while True:
    print("\n--- Passwort Manager ---")
    print("1. Passwort hinzufügen")
    print("2. Passwort abrufen")
    print("3. Passwort löschen")
    print("4. Beenden")
    wahl = input("Auswahl: ")
    
    if wahl == "1":
        passwort_hinzufuegen()
    elif wahl == "2":
        passwort_abrufen()
    elif wahl == "3":
        passwort_loeschen()
    elif wahl == "4":
        break
    else:
        print("Ungültige Auswahl.")
