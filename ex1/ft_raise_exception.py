
def input_temperature(temp_str: str) -> int:
    print(f"Input data is '{temp_str}'")
    entier = int(temp_str)
    if entier < 0:
        raise ValueError(f"{entier} is too cold for plant (min is 0)")
    elif entier > 40:
        raise ValueError(f"{entier} is too hot for plant (max is 40)")
    else:
        print(f"Temperature is now {entier} C\n")
        return entier


def test_temperature():
    try:
        input_temperature("25")
        input_temperature("abc")
    except ValueError as e:
        print(f"Caught input_temperature error:{e}\n")

    try:
        input_temperature("100")
    except ValueError as e:
        print(f"Caught input_temperature error:{e}\n")

    try:
        input_temperature("-50")
    except ValueError as e:
        print(f"Caught input_temperature error:{e}\n")

    print("All tests completed- program didn’t crash!")


def ft_raise_exception():
    print("=== Garden Temperature Checker ===\n")
    test_temperature()


if __name__ == "__main__":
    ft_raise_exception()
