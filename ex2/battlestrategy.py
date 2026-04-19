from abc import ABC, abstractmethod
from ex0 import Creature
from ex1 import HealCapability, TransformCapability
from typing import Any

class BattleStrategy(ABC):
    @abstractmethod
    def is_valid(self) -> bool:
        pass

    @abstractmethod
    def act(self) -> None:
        pass


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Any) -> bool:
        if isinstance(creature, Creature):
            return True
        return False

    def act(self, creature: Any) -> None:
        if not self.is_valid(creature):
            raise ValueError(
                "Battle error, aborting tournament: Invalid Creature "
                f"{creature.__class__.__name__} for this aggressive strategy"
                )
        print(creature.attack())


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        if isinstance(creature, TransformCapability):
            return True
        return False

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise ValueError(
                "Battle error, aborting tournament: Invalid Creature "
                f"{creature.__class__.__name__} for this aggressive strategy"
                )
        print(creature.transform())
        print(creature.attack())
        print(creature.revert())


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        if isinstance(creature, HealCapability):
            return True
        return False
    
    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise ValueError(
                "Battle error, aborting tournament: Invalid Creature "
                f"{creature.__class__.__name__} for this defensive strategy"
                )
        print(creature.attack())
        print(creature.heal(48))
    
        