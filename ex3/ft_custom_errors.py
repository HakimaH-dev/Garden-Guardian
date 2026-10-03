class GardenError(Exception):
    def __init__(self, error="Unknown garden error"):
        super().__init__(error)


class PlantError(GardenError):
    def __init__(self, error="Unknown plant error"):
        super().__init__(error)


class WaterError(GardenError):
    def __init__(self, error="Unknown water error"):
        super().__init__(error)


def test_exeption():

    try:
        print("Testing Plant Error...")
        raise PlantError("The tomato plant is wilting!\n")
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    try:
        print("Testing WaterError...")
        raise WaterError("Not enough water in the tank!\n")

    except WaterError as e:
        print(f"Caught WaterError: {e}")

    try:
        print("Testing catching all garden errors...")
        raise PlantError("The tomato plant is wilting!")

    except GardenError as e:
        print(f"Caught GardenError: {e}")

    try:
        raise WaterError("Not enough water in the tank!")

    except GardenError as e:
        print(F"Caught GardenError: {e}\n")

    print("All custom error types work correctly!")


def ft_custom_errors():
    print("=== Custom Garden Errors Demo ===")
    test_exeption()


if __name__ == "__main__":
    ft_custom_errors()
