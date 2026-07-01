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

def is_palindrome(s: str) -> bool:
    s = s.lower().replace(" ", "")
    return s == s[::-1]


def reverse_string(s: str) -> str:
    return s[::-1]


def count_vowels(s: str) -> int:
    return sum(1 for ch in s.lower() if ch in "aeiou")


def count_consonants(s: str) -> int:
    return sum(1 for ch in s.lower() if ch.isalpha() and ch not in "aeiou")


def to_snake_case(s: str) -> str:
    result = ""
    for i, ch in enumerate(s):
        if ch.isupper():
            result += "_" + ch.lower() if i > 0 else ch.lower()
        elif ch in (" ", "-"):
            result += "_"
        else:
            result += ch
    return result


def to_kebab_case(s: str) -> str:
    return to_snake_case(s).replace("_", "-")


def capitalize_words(s: str) -> str:
    return " ".join(word.capitalize() for word in s.split())


def is_anagram(s1: str, s2: str) -> bool:
    return sorted(s1.lower().replace(" ", "")) == sorted(s2.lower().replace(" ", ""))


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
    print()
    print("--- String Algorithms ---")
    print(f"is_palindrome('racecar'): {is_palindrome('racecar')}")
    print(f"is_palindrome('A man a plan a canal Panama'): {is_palindrome('A man a plan a canal Panama')}")
    print(f"reverse_string('hello'): {reverse_string('hello')}")
    print(f"count_vowels('hello world'): {count_vowels('hello world')}")
    print(f"count_consonants('hello world'): {count_consonants('hello world')}")
    print(f"to_snake_case('helloWorld'): {to_snake_case('helloWorld')}")
    print(f"to_kebab_case('helloWorld'): {to_kebab_case('helloWorld')}")
    print(f"capitalize_words('hello world from ai'): {capitalize_words('hello world from ai')}")
    print(f"is_anagram('listen', 'silent'): {is_anagram('listen', 'silent')}")
