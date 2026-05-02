from ex1 import TransformCreatureFactory, HealingCreatureFactory


def main() -> None:
    print("Testing Creature with healing capability")
    print(" base:")
    heal_factory = HealingCreatureFactory()
    heal_base = heal_factory.create_base()
    print(heal_base.describe())
    print(heal_base.attack())
    print(heal_base.heal(40))
    print(" evolved:")
    heal_env = heal_factory.create_evolved()
    print(heal_env.describe())
    print(heal_env.attack())
    print(heal_env.heal(60))
    print("\nTesting Creature with transform capability")
    print(" base:")
    trans_factory = TransformCreatureFactory()
    trans_base = trans_factory.create_base()
    print(trans_base.describe())
    print(trans_base.attack())
    print(trans_base.transform())
    print(trans_base.attack())
    print(trans_base.revert())
    print(" envolved:")
    trans_env = trans_factory.create_evolved()
    print(trans_env.describe())
    print(trans_env.attack())
    print(trans_env.transform())
    print(trans_env.attack())
    print(trans_env.revert())


if __name__ == "__main__":
    try:
        main()
    except ValueError as err:
        print(f"{err}")
    except Exception as err:
        print(f"{err}")
