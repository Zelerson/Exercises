def send_package():
    packages_sent.append(current_package.copy())
    current_package.clear()


LIMIT = 20
WEIGHT_RANGE = range(1, 11)

packages_sent = []
current_package = []
amount = int(input("Ilość paczek do wysłania: "))

for i in range(amount):
    if packages_sent and sum(packages_sent[-1]) > LIMIT:
        current_package.append(packages_sent[-1].pop(-1))

    weight = int(input("Podaj wagę: "))

    if weight not in WEIGHT_RANGE:
        send_package()
        break

    current_package.append(weight)

    if sum(current_package) > LIMIT or i+1 >= amount:
        send_package()

amount_of_packages = len(packages_sent)
total_weight = sum([sum(package) for package in packages_sent])
total_empty_weight = amount_of_packages * LIMIT - total_weight
max_empty_weight = LIMIT - sum(min(packages_sent))
most_empty = packages_sent.index(min(packages_sent)) + 1

print(f"Liczba wysłanych paczek: {amount_of_packages}")
print(f"Suma wysłancyh kilogramów: {total_weight}kg")
print(f"Suma pustych kilogramów: {total_empty_weight}kg")
print(f"Najwięcej pustych kilogramów ma paczka {most_empty} ({max_empty_weight}kg)")