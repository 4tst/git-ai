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

def is_odd(n: int) -> bool:
    return n % 2 != 0

def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def fibonacci(n: int) -> list[int]:
    if n <= 0:
        return []
    if n == 1:
        return [0]
    seq = [0, 1]
    for _ in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return seq

if __name__ == "__main__":
    print(greet("World"))
    print(f"1 + 2 = {add(1, 2)}")
    print(f"5 - 3 = {subtract(5, 3)}")
    print(f"4 * 6 = {multiply(4, 6)}")
    print(f"10 / 3 = {divide(10, 3):.2f}")
    print(f"4 is even: {is_even(4)}")
    print(f"7 is even: {is_even(7)}")
    print(f"5! = {factorial(5)}")
    print(f"fibonacci(10) = {fibonacci(10)}")
