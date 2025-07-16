from utils import (
    add_club,
    show_club,
    search_club,
    edit_club,
    delete_club
)

def izbornik():
    while True:
        print("\n IZBORNIK:")
        print("1. Dodaj novi klub")
        print("2. Prikaži sve klubove")
        print("3. Pretraži klub po nazivu")
        print("4. Uredi klub")
        print("5. Obriši klub")
        print("6. Izlaz")
        izbor = input("Odaberi opciju (1-6): ")

        if izbor == "1":
            add_club()
        elif izbor == "2":
            show_club()
        elif izbor == "3":
            naziv = input("Unesi naziv za pretragu: ")
            search_club(naziv)
        elif izbor == "4":
            edit_club()
        elif izbor == "5":
            delete_club()
        elif izbor == "6":
            print("Izlaz iz aplikacije.")
            break
        else:
            print("Nevažeći unos. Pokušaj ponovno.")

if __name__ == "__main__":
    izbornik()