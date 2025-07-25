import math_operations

# 원의 넓이
radius = 5
circle_area = math_operations.calculate_circle_area(radius)
print(f"원의 넓이: {circle_area:.2f}")

# 직사각형 넓이
width = 10
height = 5
rectangle_area = math_operations.calculate_rectangle_area(width, height)
print(f"직사각형 넓이: {rectangle_area}")

# 팩토리얼
num_factorial = 5
fact_result = math_operations.factorial(num_factorial)
print(f"팩토리얼 {num_factorial}! = {fact_result}")

# 최대공약수
num_gcd1 = 48
num_gcd2 = 18
gcd_result = math_operations.gcd(num_gcd1, num_gcd2)
print(f"최대공약수({num_gcd1}, {num_gcd2}) = {gcd_result}")