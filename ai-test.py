# AI-generated test file
def greet(name: str) -> str:
    return f"Hello, {name}!"

def farewell(name: str) -> str:
    return f"Goodbye, {name}!"

def add(a: int, b: int) -> int:
    return a + b

def subtract(a: int, b: int) -> int:
    return a - b

def multiply(a: int, b: int) -> int:
    return a * b

def divide(a: int, b: int) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def is_even(n: int) -> bool:
    return n % 2 == 0

if __name__ == "__main__":
    print(greet("World"))
    print(f"1 + 2 = {add(1, 2)}")
    print(f"5 - 3 = {subtract(5, 3)}")
    print(f"4 * 6 = {multiply(4, 6)}")
    print(f"10 / 3 = {divide(10, 3):.2f}")
    print(f"4 is even: {is_even(4)}")
    print(f"7 is even: {is_even(7)}")
