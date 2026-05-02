from abc import ABC, abstractmethod
from ex0 import Creature


class HealCapability(ABC):
    @abstractmethod
    def heal(self, target: int) -> str:
        pass


class TransformCapability(ABC):

    def __init__(self) -> None:
        self.attacks = []
        name = type(self).__name__
        self.attacks.append(f"{name} attacks normally.")

    @abstractmethod
    def transform(self) -> str:
        pass

    @abstractmethod
    def revert(self) -> str:
        pass


class Sproutling(Creature, HealCapability):
    def heal(self, target: int) -> str:
        ammount = "small amount" if target < 50 else "large amount"
        return f"Sproutling heals itself for a {ammount}"

    def attack(self) -> str:
        return "Sproutling uses Vine Whip!"


class Bloomelle(Creature, HealCapability):
    def heal(self, target: int) -> str:
        ammount = "small amount" if target < 50 else "large amount"
        return f"Bloomelle heals itself {ammount}"

    def attack(self) -> str:
        return "Bloomelle uses Petal Dance!"


class Shiftling(TransformCapability, Creature):
    def transform(self) -> str:
        self.attacks.append("Shiftling performs a boosted strike!")
        return ("Shiftling shifts into a sharper form!")

    def revert(self) -> str:
        if len(self.attacks) > 1:
            self.attacks.pop(-1)
        return "Shiftling return to normal"

    def attack(self) -> str:
        attck = self.attacks[0] if len(self.attacks) == 1 else self.attacks[1]
        return attck


class Morphagon(TransformCapability, Creature):
    def transform(self) -> str:
        self.attacks.append("Morphagon unleashes a devastating morph strike!")
        return ("Morphagon morphs into a dragonic battle form!")

    def revert(self) -> str:
        if len(self.attacks) > 1:
            self.attacks.pop(-1)
        return "Morphagon stabilizes its form."

    def attack(self) -> str:
        attack = self.attacks[0] if len(self.attacks) == 1 else self.attacks[1]
        return attack
