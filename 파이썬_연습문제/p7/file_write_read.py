file_content = """안녕하세요
파이썬 파일 처리를 연습하고 있습니다
오늘은 좋은 날씨입니다"""

file_name = "my_text_file.txt"

# 파일 쓰기
with open(file_name, 'w', encoding='utf-8') as f:
    f.write(file_content)
print("파일에 저장할 내용:")
print(file_content)

# 파일 읽기
print("\n파일에서 읽어온 내용:")
with open(file_name, 'r', encoding='utf-8') as f:
    read_content = f.read()
    print(read_content)