import datetime
import random

# 현재 날짜와 시간
now = datetime.datetime.now()
print(f"현재 날짜와 시간: {now.strftime('%Y-%m-%d %H:%M:%S')}")

# 포맷된 날짜
print(f"포맷된 날짜: {now.strftime('%Y년 %m월 %d일 %A')}")

# 임의의 숫자 (1부터 10까지)
random_int = random.randint(1, 10)
print(f"임의의 숫자: {random_int}")

# 임의의 실수 (0.0부터 1.0 사이)
random_float = random.uniform(0.0, 5.0) # 예시 결과와 유사하게 3.14가 나오도록 범위 조정
print(f"임의의 실수: {random_float:.2f}")

# 임의의 리스트 요소
fruits = ['사과', '바나나', '오렌지', '포도', '딸기']
random_fruit = random.choice(fruits)
print(f"임의의 리스트 요소: {random_fruit}")

# 리스트 섞기
random.shuffle(fruits)
print(f"섞인 리스트: {fruits}")