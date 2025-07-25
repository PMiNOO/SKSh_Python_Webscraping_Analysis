import json

data = {
    "이름": "김철수",
    "나이": 25,
    "직업": "개발자",
    "취미": ["독서", "영화감상", "코딩"],
    "주소": "서울시 강남구"
}
json_file = 'data.json'

# JSON 파일에 저장
with open(json_file, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
print(f"데이터가 {json_file}에 저장되었습니다.")

# JSON 파일에서 읽기
print("\nJSON에서 읽어온 데이터:")
with open(json_file, 'r', encoding='utf-8') as f:
    loaded_data = json.load(f)
    for key, value in loaded_data.items():
        print(f"{key}: {value}")