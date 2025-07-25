import datetime

log_content = """2025-07-20 09:00:00 - INFO - 애플리케이션 시작
2025-07-20 09:15:00 - WARNING - 메모리 사용량이 높습니다
2025-07-20 10:30:00 - ERROR - 데이터베이스 연결 실패
2025-07-20 11:00:00 - INFO - 사용자 로그인: user123
2025-07-20 11:45:00 - ERROR - 파일을 찾을 수 없음
2025-07-20 12:00:00 - WARNING - 디스크 공간 부족
2025-07-20 13:00:00 - INFO - 백업 완료
"""

log_file = "application.log"

# 로그 파일 생성
with open(log_file, 'w', encoding='utf-8') as f:
    f.write(log_content)
print("로그 파일이 생성되었습니다.")

# ERROR 레벨 로그 필터링
print("\nERROR 레벨 로그들:")
with open(log_file, 'r', encoding='utf-8') as f:
    for line in f:
        if "ERROR" in line:
            print(line.strip())

# WARNING 레벨 로그 필터링
print("\nWARNING 레벨 로그들:")
with open(log_file, 'r', encoding='utf-8') as f:
    for line in f:
        if "WARNING" in line:
            print(line.strip())