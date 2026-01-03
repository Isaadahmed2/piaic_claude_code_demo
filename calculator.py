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


def factorial(a):
    if a < 0:
        raise ValueError("Cannot compute factorial of negative number")
    if not a.is_integer():
        raise ValueError("Factorial requires an integer input")
    return math.factorial(int(a))


def log(a):
    if a <= 0:
        raise ValueError("Logarithm argument must be positive")
    return math.log(a)


def log10(a):
    if a <= 0:
        raise ValueError("Log10 argument must be positive")
    return math.log10(a)


def log2(a):
    if a <= 0:
        raise ValueError("Log2 argument must be positive")
    return math.log2(a)


def exp(a):
    return math.exp(a)


def sin(a):
    return math.sin(math.radians(a))


def cos(a):
    return math.cos(math.radians(a))


def tan(a):
    result = math.tan(math.radians(a))
    if abs(result) > 1e15:
        raise ValueError("Tangent is undefined at odd multiples of 90 degrees")
    return result


def asin(a):
    if a < -1 or a > 1:
        raise ValueError("Asin argument must be between -1 and 1")
    return math.degrees(math.asin(a))


def acos(a):
    if a < -1 or a > 1:
        raise ValueError("Acos argument must be between -1 and 1")
    return math.degrees(math.acos(a))


def atan(a):
    return math.degrees(math.atan(a))


def sinh(a):
    return math.sinh(a)


def cosh(a):
    return math.cosh(a)


def tanh(a):
    return math.tanh(a)


def degrees(a):
    return math.degrees(a)


def radians(a):
    return math.radians(a)


def floor(a):
    return math.floor(a)


def ceil(a):
    return math.ceil(a)


def fabs(a):
    return math.fabs(a)


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def get_operation():
    print("\nSelect operation:")
    print("=== Basic Operations ===")
    print("1.  Add (+)")
    print("2.  Subtract (-)")
    print("3.  Multiply (*)")
    print("4.  Divide (/)")
    print("5.  Modulo (%)")
    print("6.  Power (^)")
    print("=== Scientific Functions ===")
    print("7.  Square Root (sqrt)")
    print("8.  Factorial (n!)")
    print("9.  Logarithm (ln)")
    print("10. Log10")
    print("11. Log2")
    print("12. Exponential (e^x)")
    print("13. Sine (sin)")
    print("14. Cosine (cos)")
    print("15. Tangent (tan)")
    print("16. Inverse Sine (asin)")
    print("17. Inverse Cosine (acos)")
    print("18. Inverse Tangent (atan)")
    print("19. Hyperbolic Sine (sinh)")
    print("20. Hyperbolic Cosine (cosh)")
    print("21. Hyperbolic Tangent (tanh)")
    print("22. Floor")
    print("23. Ceiling")
    print("24. Absolute Value (abs)")
    print("q.  Quit")

    while True:
        choice = input("\nEnter choice (1-24 or q): ").strip()
        if choice.lower() == 'q':
            return None
        if choice in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                      '11', '12', '13', '14', '15', '16', '17', '18', '19',
                      '20', '21', '22', '23', '24'):
            return choice
        print("Invalid choice. Please enter 1-24 or q.")


def main():
    print("=" * 45)
    print("       Python Scientific Calculator")
    print("=" * 45)

    while True:
        operation = get_operation()

        if operation is None:
            print("\nThank you for using the calculator. Goodbye!")
            break

        # Single operand operations (7-24)
        if operation in ('7', '8', '9', '10', '11', '12', '13', '14', '15',
                         '16', '17', '18', '19', '20', '21', '22', '23', '24'):
            a = get_number("Enter number: ")
            try:
                if operation == '7':
                    result = square_root(a)
                    print(f"sqrt({a}) = {result}")
                elif operation == '8':
                    result = factorial(a)
                    print(f"{int(a)}! = {result}")
                elif operation == '9':
                    result = log(a)
                    print(f"ln({a}) = {result}")
                elif operation == '10':
                    result = log10(a)
                    print(f"log10({a}) = {result}")
                elif operation == '11':
                    result = log2(a)
                    print(f"log2({a}) = {result}")
                elif operation == '12':
                    result = exp(a)
                    print(f"e^{a} = {result}")
                elif operation == '13':
                    result = sin(a)
                    print(f"sin({a}°) = {result}")
                elif operation == '14':
                    result = cos(a)
                    print(f"cos({a}°) = {result}")
                elif operation == '15':
                    result = tan(a)
                    print(f"tan({a}°) = {result}")
                elif operation == '16':
                    result = asin(a)
                    print(f"asin({a}) = {result}°")
                elif operation == '17':
                    result = acos(a)
                    print(f"acos({a}) = {result}°")
                elif operation == '18':
                    result = atan(a)
                    print(f"atan({a}) = {result}°")
                elif operation == '19':
                    result = sinh(a)
                    print(f"sinh({a}) = {result}")
                elif operation == '20':
                    result = cosh(a)
                    print(f"cosh({a}) = {result}")
                elif operation == '21':
                    result = tanh(a)
                    print(f"tanh({a}) = {result}")
                elif operation == '22':
                    result = floor(a)
                    print(f"floor({a}) = {result}")
                elif operation == '23':
                    result = ceil(a)
                    print(f"ceil({a}) = {result}")
                elif operation == '24':
                    result = fabs(a)
                    print(f"abs({a}) = {result}")
            except ValueError as e:
                print(f"Error: {e}")
        else:
            # Two operand operations (1-6)
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
