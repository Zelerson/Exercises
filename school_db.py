class User:
    def __init__(self, name: str, group: list, subject: str):
        self.name = name
        self.group = group
        self.subject = subject

    def __str__(self):
        return self.name


students = []
teachers = []
sup_teachers = []

while True:
    print("Dostępne komendy: utwórz, zarządzaj, koniec")
    command = input("Podaj komendę: \n")
    match command:
        case "utwórz":
            while True:
                print("Dostępne komendy: uczeń, nauczyciel, wychowawca, koniec")
                command = input("Podaj komendę: \n")
                match command:
                    case "uczeń":
                        name = input("Podaj imię i nazwisko ucznia: \n")
                        group = input("Podaj klasę ucznia: \n")
                        students.append(User(name, group, None))

                    case "nauczyciel":
                        name = input("Podaj imię i nazwisko nauczyciela: \n")
                        subject = input("Podaj nazwę prowadzonego przedmiotu: \n")
                        groups = []

                        while True:
                            group = input("Podaj prowadzoną klasę: \n")
                            if group == "":
                                break
                            groups.append(group)

                        teachers.append(User(name, groups, subject.lower()))

                    case "wychowawca":
                        name = input("Podaj imię i nazwisko wychowawcy: \n")
                        group = input("Podaj prowadzoną klasę: \n")
                        sup_teachers.append(User(name, group, None))

                    case "koniec":
                        break

        case "zarządzaj":
            while True:
                print(
                    "Dostępne komendy: klasa, uczeń, nauczyciel, " "wychowawca, koniec"
                )
                command = input("Podaj komendę: \n")

                match command:
                    case "klasa":
                        searched_group = input("Podaj nazwę wyszukiwanej klasy: \n")
                        if any(x for x in students if x.group == searched_group):
                            print(f"Do klasy {searched_group} uczęszczają: ")

                            for student in students:
                                if student.group == searched_group:
                                    print(student)
                            print("Wychowawca klasy: ")

                            for sup_teacher in sup_teachers:
                                if sup_teacher.group == searched_group:
                                    print(sup_teacher)
                        else:
                            print("Brak podanej klasy")

                    case "uczeń":
                        searched_student = input(
                            "Podaj imię i nazwisko wyszukiwanego ucznia: \n"
                        )
                        if any(x for x in students if x.name == searched_student):
                            print("Lekcje oraz nauczyciele prowadzący: ")

                            for student in students:
                                if student.name == searched_student:
                                    student_group = student.group

                            student_subjects = [
                                f"{x.subject}: {x.name}"
                                for x in teachers
                                if student_group in x.group
                            ]

                            for subject in student_subjects:
                                print(subject)
                        else:
                            print("Brak podanego ucznia")

                    case "nauczyciel":
                        searched_teacher = input(
                            "Podaj imię i nazwisko wyszukiwanego nauczyciela: \n"
                        )
                        if any(x for x in teachers if x.name == searched_teacher):
                            print("Prowadzone klasy: ")
                            for teacher in teachers:
                                if teacher.name == searched_teacher:
                                    for group in teacher.group:
                                        print(group)
                        else:
                            print("Brak podanego nauczyciela")

                    case "wychowawca":
                        searched_sup = input(
                            "Podaj imię i nazwisko wyszukiwanego wychowawcy: \n"
                        )
                        if any(x for x in sup_teachers if x.name == searched_sup):
                            for sup in sup_teachers:
                                if sup.name == searched_sup:
                                    sup_group = sup.group

                            sup_pupils = [x for x in students if x.group == sup_group]
                            print("Prowadzeni uczniowie: ")

                            for student in sup_pupils:
                                print(student)
                        else:
                            print("Brak podanego wychowawcy")

                    case "koniec":
                        break

        case "koniec":
            break
