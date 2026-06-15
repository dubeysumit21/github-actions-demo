def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


if __name__ == "__main__":
    print("App running")
    print(f"add(2, 3) = {add(2, 3)}")
    print(f"multiply(4, 5) = {multiply(4, 5)}")
