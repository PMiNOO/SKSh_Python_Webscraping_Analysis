text = "Python is awesome programming language"
words = text.split()

print(f"원본 문자열: {text}")
print(f"분리된 단어들: {words}")
print(f"하이픈으로 연결: {'-'.join(words)}")
print(f"대문자로 변환 후 공백으로 연결: {' '.join([word.upper() for word in words])}")