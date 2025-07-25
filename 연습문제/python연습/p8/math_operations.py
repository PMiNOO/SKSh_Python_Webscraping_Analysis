import math

def calculate_circle_area(radius):
    return math.pi * (radius ** 2)

def calculate_rectangle_area(width, height):
    return width * height

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a