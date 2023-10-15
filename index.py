def navigator(attr):
    for i in range(len(attr)):
        print(attr[i])


class Intern:
    def __init__(self, _table, name, notes):
        self.name = name
        self.notes = notes
        self.tab = _table
        _table.interns.append(self)

    def means(self):
        sum = 0
        for note in self.notes:
            sum += note
        return sum / len(self.notes)


class Table:
    def __init__(self, notes_size):
        self.interns = []
        self.notes_size = notes_size

    def add(self, n):
        for i in range(n):
            navigator(["_" * 20, f"Stagiaire {i + 1}/{n}"])
            name = input("Nom et Prénom: ")
            notes = []
            for j in range(self.notes_size):
                notes.append(float(input(f"Note {j + 1} = ")))
            Intern(self, name, notes)
        self.options()

    def delete(self, index):
        del self.interns[index]
        self.options()

    def sort(self, param, _order):
        if _order == 0:
            self.options(3)
        reverse = False
        if _order == 1:
            reverse = True
        elif _order == 2:
            reverse = False

        elements = []
        for j in range(len(self.interns)):
            if param == 1:
                elements.append([self.interns[j].name, self.interns[j].notes])
            elif param == 2:
                elements.append([self.interns[j].means(), self.interns[j].name, self.interns[j].notes])
        elements.sort(reverse=reverse)
        new_tab = []
        for j in range(len(elements)):
            if param == 1:
                new_tab.append(Intern(self, elements[j][0], elements[j][1]))
            elif param == 2:
                new_tab.append(Intern(self, elements[j][1], elements[j][2]))
        self.interns = new_tab

    def options(self, opt=None):
        num_option = 0
        if opt is None:
            navigator([
                "_" * 20,
                f"▪ Les stagiaires sont {len(self.interns)}",
                "1 - Ajouter des Stagiaires",
                "2 - Supprimer des Stagiaires",
                "3 - Moyenne des Stagiaires",
                f"4 - Changer Unité des notes({self.notes_size})",
                "0 - Quitter"
            ])
            num_option = int(input("Choisir: "))
        elif opt is not None:
            num_option = opt

        if num_option == 1:
            size_intern = int(input("Nombre de stagiaire: "))
            self.add(size_intern)
        elif num_option == 2:
            if len(self.interns) > 0:
                navigator(["_" * 20, "▪ Si vous voulez retourner appuyez sur la touche Entrée"])
                for i in range(len(self.interns)):
                    navigator([f"{i} - {self.interns[i].name}"])
                inp = input("Choisir: ")
                if inp != '':
                    index = int(inp)
                    self.delete(index)
                else:
                    self.options()
            else:
                navigator(["_" * 20, "Vide.", "0 - Retourner"])
                if int(input("Choisir: ")) == 0:
                    self.options()
        elif num_option == 3:
            if len(self.interns) > 0:
                print("_" * 20)
                for i in range(len(self.interns)):
                    navigator([
                        f"Nom: {self.interns[i].name}, "
                        f"Notes: {self.interns[i].notes}, "
                        f"Moyenne: {self.interns[i].means()}"
                    ])
                navigator(["1 - Trier par", "0 - Retourner"])
                num_option = int(input("Choisir: "))
                if num_option == 1:
                    navigator(["_" * 20, "1 - Nom", "2 - Moyenne", "0 - Retourner"])
                    num_option = int(input("Choisir: "))
                    if num_option == 0:
                        self.options(3)
                    else:
                        navigator(["_" * 20, "1 - Ordre Croissant", "2 - Ordre Décroissant", "0 - Retourner"])
                        order = int(input("Choisir: "))
                        self.sort(num_option, order)
                        self.options(3)
                elif num_option == 0:
                    self.options()

            else:
                navigator(["_" * 20, "Vide.", "0 - Retourner"])
                if int(input("Choisir: ")) == 0:
                    self.options()
        elif num_option == 4:
            notes_size = int(input("Nombre d'unité: "))
            self.notes_size = notes_size
            self.options()
        elif num_option == 0:
            return


table = Table(2)
table.options()
