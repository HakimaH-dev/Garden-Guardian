def garden_operation(op: int) -> None:
    if op == 0:
        print(f"Testing operation {op}...")
        int("abc")
    elif op == 1:
        print(f"Testing operation {op}...")
        5 / 0
    elif op == 2:
        print(f"Testing operation {op}...")
        open("/non/existent/file")
    elif op == 3:
        print(f"Testing operation {op}...")
        "mimi" - 34
    else:
        print(f"Testing operation {op}...")
        print("Operation completed successfully!\n")


def test_error_types():
    try:
        garden_operation(0)
    except ValueError as e:
        print(f"Caught ValueError: {e}\n")

    try:
        garden_operation(1)
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}\n")

    try:
        garden_operation(2)
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}\n")

    try:
        garden_operation(3)

    except TypeError as e:
        print(f"Caught TypeError: {e}\n")

        garden_operation(4)

    print("All error types tested successfully!")


def ft_differente_errors():
    print("=== Garden Error Types Demo ===")
    test_error_types()


if __name__ == "__main__":
    ft_differente_errors()
