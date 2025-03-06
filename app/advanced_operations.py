import math

def power(base, exp):
    return base ** exp

def square_root(num):
    if num < 0:
        return "Error! Square root of negative number."
    return math.sqrt(num)

def logarithm(num, base=10):
    if num <= 0:
        return "Error! Logarithm of non-positive number."
    return math.log(num, base)

def factorial(num):
    if num < 0:
        return "Error! Factorial of negative number."
    return math.factorial(num)
