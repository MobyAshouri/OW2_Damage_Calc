import json

class ability:
    def __init__(self, charName, abilityNumber) -> None:
        with open("characters.json", "r") as file:
            data = json.load(file)

        self.name = data[charName][f"a{abilityNumber}"]["name"]

        try:
            self.damage = data[charName][f"a{abilityNumber}"]["damage"]
        except (KeyError):
            self.damage = 0
        
        try:
            self.healing = data[charName][f"a{abilityNumber}"]["healing"]
        except (KeyError):
            self.healing = 0
    
    def __str__(self) -> str:
        return f"===============\nABILITY NAME: {self.name}\nABILITY DAMAGE: {self.damage}\nABILITY HEALING: {self.healing}\n===============\n"

class weapon:
    def __init__(self, charName) -> None:

        with open("characters.json", "r") as file:
            data = json.load(file)

        self.name = data[charName]["weapon"]["name"]
        try:
            self.damage = data[charName]["weapon"]["damage"]
        except (KeyError):
            self.damage = 0

        try:
            self.healing = data[charName]["weapon"]["healing"]
        except (KeyError):
            self.healing = 0

        try:
            self.reloadTime = data[charName]["weapon"]["reload time"]
        except (KeyError):
            self.reloadTime = None


    def __str__(self) -> str:
        return f"===============\nWEAPON NAME: {self.name}\nWEAPON DAMAGE: {self.damage}\nWEAPON HEALING: {self.healing}\n===============\n"

class hero:
    def __init__(self, name = 'ana') -> None:
        with open("characters.json", "r") as file:
            data = json.load(file)

        self.name = name
        self.weapon = weapon(self.name)
        self.abilities = [ability(self.name, i) for i in range(1, len(data[self.name].keys()))]

    def __str__(self) -> str:
        
        string = ''
        for ability in self.abilities:
            string+=ability.__str__()

        return self.weapon.__str__() + string
