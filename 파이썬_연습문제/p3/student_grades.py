student_grades = {
    '김철수': 85,
    '이영희': 92,
    '박민수': 78,
    '최수진': 95
}

total_score = sum(student_grades.values())
average_score = total_score / len(student_grades)

print("학생 성적:")
for name, score in student_grades.items():
    print(f"{name}: {score}점")
print(f"평균 점수: {average_score:.1f}점")