
def input_temperature(temp_str: str) -> int:
    entier = int(temp_str)
    print(f"Input data is '{temp_str}'")
    print(f"Temperature is now {entier} C\n")
    return entier


def test_temperature():
    try:
        input_temperature("25")
        input_temperature("abc")
    except ValueError as e:
        print(f"Caught input_temperature error:{e}\n")

    print("All tests completed- program didn’t crash!")


def ft_first_exception():
    print("=== Garden Temperature ===\n")
    test_temperature()


if __name__ == "__main__":
    ft_first_exception()
