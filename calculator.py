#!/usr/bin/env python3
"""A simple arithmetic calculator CLI."""

import math


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


def modulo(a, b):
    if b == 0:
        raise ValueError("Cannot compute modulo by zero")
    return a % b


def power(a, b):
    return a ** b


def square_root(a):
    if a < 0:
        raise ValueError("Cannot compute square root of negative number")
    return math.sqrt(a)


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def get_operation():
    print("\nSelect operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Modulo (%)")
    print("6. Power (^)")
    print("7. Square Root (sqrt)")
    print("q. Quit")

    while True:
        choice = input("\nEnter choice (1-7 or q): ").strip()
        if choice.lower() == 'q':
            return None
        if choice in ('1', '2', '3', '4', '5', '6', '7'):
            return choice
        print("Invalid choice. Please enter 1-7 or q.")


def main():
    print("=" * 40)
    print("      Python Arithmetic Calculator")
    print("=" * 40)

    while True:
        operation = get_operation()

        if operation is None:
            print("\nThank you for using the calculator. Goodbye!")
            break

        if operation == '7':
            a = get_number("Enter number: ")
            try:
                result = square_root(a)
                print(f"sqrt({a}) = {result}")
            except ValueError as e:
                print(f"Error: {e}")
        else:
            a = get_number("Enter first number: ")
            b = get_number("Enter second number: ")

            try:
                if operation == '1':
                    result = add(a, b)
                    symbol = '+'
                elif operation == '2':
                    result = subtract(a, b)
                    symbol = '-'
                elif operation == '3':
                    result = multiply(a, b)
                    symbol = '*'
                elif operation == '4':
                    result = divide(a, b)
                    symbol = '/'
                elif operation == '5':
                    result = modulo(a, b)
                    symbol = '%'
                elif operation == '6':
                    result = power(a, b)
                    symbol = '^'

                print(f"\n{a} {symbol} {b} = {result}")
            except ValueError as e:
                print(f"Error: {e}")


if __name__ == "__main__":
    main()
