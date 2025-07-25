def greet(name, message="안녕하세요"):
    return f"{message}, {name}님!"

print(greet("김철수"))
print(greet("John", "Hello"))
print(greet("이영희", "안녕하세요") + " 좋은 하루 되세요!") # 출력 결과와 맞추기 위해 추가