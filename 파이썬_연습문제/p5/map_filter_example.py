numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squared_numbers = list(map(lambda x: x**2, numbers))
filtered_numbers = list(filter(lambda x: x > 5, numbers))
filtered_and_squared = list(map(lambda x: x**2, filter(lambda x: x > 5, numbers)))

print(f"원본 숫자: {numbers}")
print(f"모든 수의 제곱: {squared_numbers}")
print(f"5보다 큰 수들: {filtered_numbers}")
print(f"5보다 큰 수들의 제곱: {filtered_and_squared}")