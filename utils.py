import json
import os
from models import Klub

DATA_FILE = "clubs.json"


def read_club():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            return [Klub.from_dict(d) for d in data]
    return []
    

def save_club(clubs):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump([k.to_dict() for k in clubs], f, indent=2, ensure_ascii=False)


def add_club():
    name = input("Naziv kluba: ")
    description = input("Opis kluba: ")
    stadium = input("Stadion kluba: ")
    location = input("Lokacija kluba: ")
    foundation = input("Osnivanje kluba: ")

    new_klub = Klub(name, description, stadium, location, foundation)
    clubs = read_club()
    clubs.append(new_klub)
    save_club(clubs)
    print("Klub dodan!")

def show_club():
    clubs = read_club()
    if not clubs:
        print("Nema unešenog kluba")
        return
    
    for i, klub in enumerate(clubs, 1):
        print(f"\n--- klub#{i} ---")
        print(klub)


def search_club(find_club):
    clubs = read_club()
    found_club = [k for k in clubs if find_club.lower() in k.name.lower()]
    if not found_club:
        print("Nema rezultata za taj naziv")
    else:
        for klub in found_club:
            print(f"\n{klub}")


def edit_club():
    clubs = read_club()
    show_club()
    try:
        index = int(input("\nUnesi broj kluba koji želiš urediti: ")) - 1
        if index < 0 or index >= len(clubs):
            print("Nevažeći broj.")
            return
        klub = clubs[index]
        print("\nPritisni Enter za zadržavanje postojeće vrijednosti.")
        klub.name = input(f"Naziv ({klub.name}): ") 
        klub.description = input(f"Opis ({klub.description}): ") 
        klub.stadium = input(f"Stadion ({klub.stadium}): ") 
        klub.location = input(f"Lokacija ({klub.location}): ") 
        klub.foundation = input(f"Godina osnutka ({klub.foundation}): ")
        save_club(clubs)
        print("Klub uspješno uređen.")
    except ValueError:
        print("Nevažeći unos.")


def delete_club():
    clubs = read_club()
    show_club()
    try:
        index = int(input("\nUnesi broj kluba koji želiš obrisati: ")) - 1
        if index < 0 or index >= len(clubs):
            print("Nevažeći broj.")
            return
        potvrda = input(f" Sigurno želiš obrisati '{clubs[index].name}'? (da/ne): ")
        if potvrda.lower() == "da":
            del clubs[index]
            save_club(clubs)
            print("Klub obrisan.")
        else:
            print("Brisanje otkazano.")
    except ValueError:
        print("Nevažeći unos.")