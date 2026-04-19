from abc import ABC, abstractmethod
from ex0 import Creature
from ex1 import HealCapability, TransformCapability


class BattleStrategy(ABC):
    @abstractmethod
    def is_valid(self) -> bool:
        pass

    @abstractmethod
    def act(self) -> None:
        pass


class NormalStrategy(BattleStrategy, Creature):
    def is_valid(self):
        return super().is_valid()

    def act(self):
        return super().act()

    def attack(self):
        return super().attack()


class AggressiveStrategy(BattleStrategy, TransformCapability, Creature):
    def transform(self):
        return super().transform()

    def revert(self):
        return super().revert()

    def attack(self):
        return super().attack()


class DefensiveStrategy(BattleStrategy, HealCapability, Creature):
    def heal(self, target):
        return super().heal(target)

    def attack(self):
        return super().attack()
