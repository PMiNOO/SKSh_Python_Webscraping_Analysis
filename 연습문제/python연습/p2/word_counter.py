sentence = input("문장을 입력하세요: ")

words = sentence.split()
print(f"공백 제거: {sentence}") # 출력 결과 예시와 동일하게 원본 문자열 출력
print(f"단어 개수: {len(words)}개")