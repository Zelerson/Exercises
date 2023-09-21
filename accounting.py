balance = 0
warehouse = []
history = []


def check_balance():
    global balance
    return balance


def check_warehouse():
    for product in warehouse:
        for k, v in product.items():
            print(f"{k.capitalize()}: {v}")


def check_item(name: str):
    for product in warehouse:
        if product["produkt"] == name.lower():
            print(f"Ilość: {product['ilość']}")
            print(f"Cena: {product['cena']}")
            break
    else: print(f"Nie znaleziono produktu {name}")


def change_balance(amount: int):
    global balance
    if not balance + amount < 0:
        balance += amount
        history.append(f"Saldo: {amount}")
        return True
    return False


def purchase(name: str, price: int, quantity: int):
    product = {"produkt": name.lower(),
               "cena": price,
               "ilość": quantity}
    if change_balance(-price * quantity):
        if not any(d["produkt"] == name.lower() for d in warehouse):
            warehouse.append(product)
            history.append(f"Zakup: {name}, {price} x {quantity}")
            return True
        else:
            for item in warehouse:
                if item["produkt"] == name.lower():
                    item["ilość"] += quantity
                    history.append(f"Zakup: {name}, {price} x {quantity}")
                    return True
    return False


def check_history(fr, to):
    if fr is not None:
        fr = int(fr)
    if to is not None:
        to = int(to)
    for e in history[fr:to]:
        print(e)


def sale(name: str, price: int, quantity: int):
    if any(d["produkt"] == name.lower() for d in warehouse):
        for item in warehouse:
            if item["produkt"] == name.lower() and item["ilość"] >= quantity:
                item["ilość"] -= quantity
                change_balance(price * quantity)
                if item["ilość"] == 0:
                    warehouse.remove(item)
                history.append(f"Sprzedaż: {name}, {price} x {quantity}")
                return True
    return False


while True:
    print("Lista komend: \n"
          "saldo\n"
          "sprzedaż\n"
          "zakup\n"
          "konto\n"
          "lista\n"
          "magazyn\n"
          "przegląd\n"
          "koniec\n")

    command = input("Wprowadź komendę: ")

    match command:
        case "saldo":
            try:
                saldo = input("Podaj kwotę do dodania lub odjęcia z konta: ")
                change_balance(int(saldo))
            except:
                print("Błędna kwota")
        case "sprzedaż":
            try:
                produkt = input("Podaj nazwę produktu w magazynie: ")
                cena = input("Podaj cenę produktu")
                ilosc = input("Podaj ilość sprzedanych sztuk")
                sale(produkt, int(cena), int(ilosc))
            except:
                print("Wprowadzono błędne dane. \n"
                      "Produkt musi znajdować się w magazynie. \n"
                      "Cena i ilość nie mogą być ujemne.")
        case "zakup":
            try:
                produkt = input("Podaj nazwę produktu w magazynie: ")
                cena = input("Podaj cenę produktu")
                ilosc = input("Podaj ilość sprzedanych sztuk")
                purchase(produkt, int(cena), int(ilosc))
            except:
                print("Wprowadzono błędne dane. \n"
                      "Cena i ilość nie mogą być ujemne.")
        case "konto":
            check_balance()
        case "lista":
            check_warehouse()
        case "magazyn":
            produkt = input("Wprowadź nazwę wyszukiwanego produktu")
            check_item(produkt)
        case "przegląd":
            try:
                od = input("Wprowadź wartość początkową (zaczynając od 0): ")
                do = input("Wprowadź wartość końcową: ")
                if od == "":
                    od = None
                if do == "":
                    do = None
                if int(od) > len(history) or int(do) > len(history):
                    print(f"Dostępny przedział to 0 - {len(history)} - 1")
                else:
                    check_history(od, do)
            except:
                print("Wprowadzono błędne dane. \n"
                      "Wprowadź liczby lub brak wartości (Enter) \n"
                      f"Dostępny przedział to 0 - {len(history) - 1}")
        case "koniec":
            break
        case _:
            print("Błędna komenda \n")
