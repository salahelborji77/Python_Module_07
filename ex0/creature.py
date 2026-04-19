from abc import ABC, abstractmethod


class Creature(ABC):
    @abstractmethod
    def attack(self) -> str:
        pass

    def describe(self) -> str:
        elements = {
            "Flameling": "Fire",
            "Aquabub": "Water",
            "Pyrodon": "Fire/Flying",
            "Torragon": "Water",
            "Sproutling": "Grass",
            "Bloomelle": "Grass/Fairy",
            "Shiftling": "Normal",
            "Morphagon": "Normal/Dragon"
        }
        key_ele = self.__class__.__name__
        return f"{key_ele} is a {elements[key_ele]} type Creature"


class Flameling(Creature):
    def attack(self) -> str:
        return "Flameling uses Ember!"


class Pyrodon(Creature):
    def attack(self) -> str:
        return "Pyrodon uses Flamethrower!"


class Aquabub(Creature):
    def attack(self) -> str:
        return "Aquabub uses Water Gun!"


class Torragon(Creature):
    def attack(self) -> str:
        return "Torragon uses Hydro Pump!"
