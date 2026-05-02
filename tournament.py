from ex0 import FlameFactory, AquaFactory, CreatureFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    NormalStrategy,
    AggressiveStrategy,
    DefensiveStrategy,
    BattleStrategy
)


def battle(
        first: tuple[CreatureFactory, BattleStrategy],
        second: tuple[CreatureFactory, BattleStrategy],
        ) -> None:
    print("\n* Battle *")
    fac_1, strg_1 = first
    fac_2, strg_2 = second
    creature_1 = fac_1.create_base()
    creature_2 = fac_2.create_base()
    print(creature_1.describe())
    print(" vs.")
    print(creature_2.describe())
    print(" now fight!")
    try:
        strg_1.act(creature_1)
        strg_2.act(creature_2)
    except ValueError as err:
        print(f"{err}")


def iter_test(test: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    print("*** Tournament ***")
    print(f"{len(test)} opponents involved")
    for i in range(len(test)):
        for j in range(i + 1, len(test)):
            battle(test[i], test[j])


def main() -> None:
    basic = [
        (FlameFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy())
    ]

    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")
    iter_test(basic)
    error = [
        (FlameFactory(), AggressiveStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy())
    ]
    print("\nTournament 1 (error)")
    print("[ (Flameling+Aggressive), (Healing+Defensive) ]")
    iter_test(error)
    multiple = [
        (AquaFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
        (TransformCreatureFactory(), AggressiveStrategy())
    ]
    print("\nTournament 2 (multiple))")
    print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    iter_test(multiple)


if __name__ == "__main__":
    try:
        main()
    except ValueError as err:
        print(f"{err}")
    except Exception as err:
        print(f"{err}")
