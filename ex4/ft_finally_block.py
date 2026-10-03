class PlantError(Exception):
    def __init__(self, error="Unknown plant error"):
        super().__init__(error)


def water_plant(plant_name: str):
    if plant_name != plant_name.capitalize():
        raise PlantError(f"Invalid plant name to water: {plant_name}")
    else:
        print(f"Watering {plant_name}: [OK]")


def test_watering_system():
    try:
        print("Testing valid plants")
        print("Opening watering system")
        water_plant("Tomato")
        water_plant("Lettuce")
        water_plant("Carrote")

    except PlantError as e:
        print(f"Caught PlantError: {e}")

    finally:
        print("Closing watering system\n")

    try:
        print("Testing invalid plants")
        print("Opening watering system")
        water_plant("Tomato")
        water_plant("lettuce")
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print("... ending tests and returning to main")
        return

    finally:
        print("Closing watering system\n")

        print("Cleanup always happens, even with errors!")


def ft_finally_block():
    print("=== Garden Watering System ===\n")
    test_watering_system()


if __name__ == "__main__":
    ft_finally_block()
