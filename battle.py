from ex0 import CreatureFactory, FlameFactory, AquaFactory


def handler_creature(creature: CreatureFactory) -> None:
    if not isinstance(creature, CreatureFactory):
        raise ValueError("Invalid creature factory.")
    base = creature.create_base()
    print(base.describe())
    print(base.attack())
    evolved = creature.create_evolved()
    print(evolved.describe())
    print(evolved.attack())


def handler_battle(
            fac_creature1: CreatureFactory,
            fac_creature2: CreatureFactory
        ) -> None:
    if (
            not isinstance(fac_creature1, CreatureFactory)
            or not isinstance(fac_creature2, CreatureFactory)
    ):
        raise ValueError("Invalid creature factory.")
    base1 = fac_creature1.create_base()
    base2 = fac_creature2.create_base()
    print(base1.describe())
    print(" vs.")
    print(base2.describe())
    print(" fight!")
    print(base1.attack())
    print(base2.attack())


def main() -> None:
    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()

    print("Testing factory")
    handler_creature(flame_factory)
    print("\nTesting factory")
    handler_creature(aqua_factory)
    print("\nTesting battle")
    handler_battle(flame_factory, aqua_factory)


if __name__ == "__main__":
    try:
        main()
    except ValueError as err:
        print(f"{err}")
    except Exception as err:
        print(f"{err}")
