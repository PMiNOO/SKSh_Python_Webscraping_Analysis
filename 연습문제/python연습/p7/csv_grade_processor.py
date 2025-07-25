import csv

student_data = [
    ['김철수', 85],
    ['이영희', 92],
    ['박민수', 78],
    ['최수진', 95]
]
csv_file = 'grades.csv'

# CSV 파일에 저장
with open(csv_file, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(student_data)
print(f"학생 성적이 {csv_file}에 저장되었습니다.")

# CSV 파일에서 읽고 평균 계산
total_score = 0
student_count = 0
print("\n성적 분석 결과:")
with open(csv_file, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        name = row[0]
        score = int(row[1])
        print(f"{name}: {score}점")
        total_score += score
        student_count += 1

overall_average = total_score / student_count
print(f"전체 평균: {overall_average:.1f}점")