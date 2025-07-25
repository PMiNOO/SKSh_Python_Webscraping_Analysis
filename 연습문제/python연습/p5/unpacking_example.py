# 튜플 언패킹
coordinates = (10, 20)
x, y = coordinates
print(f"좌표: x={x}, y={y}")

# 리스트 언패킹
numbers_list = [1, 2, 3]
a, b, c = numbers_list
print(f"리스트 언패킹: a={a}, b={b}, c={c}")

# *args (가변 위치 인수)
def sum_all(*args):
    return sum(args)

print(f"가변 인수의 합: {sum_all(10, 20, 30)}")

# **kwargs (가변 키워드 인수)
def print_info(**kwargs):
    info_parts = []
    for key, value in kwargs.items():
        info_parts.append(f"{key}={value}")
    print(f"키워드 인수들: {', '.join(info_parts)}")

print_info(name='김철수', age=25, city='서울')