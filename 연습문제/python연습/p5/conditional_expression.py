# conditional_expression.py

# 삼항 연산자 (if-else in one line)
score = 85
result = "합격" if score >= 80 else "불합격"
print(f"점수: {score}, 결과: {result}")

age = 17
status = "성인" if age >= 19 else "미성년자"
print(f"나이: {age}, 상태: {status}")

# 리스트 컴프리헨션 내 조건부 표현식
numbers = [5, -3, 12, 0, -8, 23]
positive_numbers = [num for num in numbers if num > 0]
print(f"양수들: {positive_numbers}")

# max() 함수와 함께 사용 (예시 결과에 "숫자들의 최대값: 42"가 있어 추가)
num1, num2, num3 = 10, 42, 20
max_val = num1 if num1 > num2 and num1 > num3 else (num2 if num2 > num3 else num3)
print(f"숫자들의 최대값: {max_val}")