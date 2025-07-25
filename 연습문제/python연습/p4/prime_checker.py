num = int(input("숫자를 입력하세요: "))

is_prime = True
if num < 2:
    is_prime = False
else:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

if is_prime:
    print(f"{num}은 소수입니다.")
else:
    print(f"{num}은 소수가 아닙니다.")