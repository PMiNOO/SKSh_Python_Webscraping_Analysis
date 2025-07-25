import os
import sys

print(f"현재 작업 디렉토리: {os.getcwd()}")
print(f"Python 버전: {sys.version}")
print(f"운영체제: {sys.platform}")

# 환경 변수 PATH 일부 (Windows에서는 Path, Linux/macOS에서는 PATH)
# 예시 결과에 맞춰 'PATH'로 통일
path_env = os.environ.get('PATH')
if path_env:
    # PATH 환경 변수의 첫 번째 몇 개 항목만 출력 (너무 길어질 수 있으므로)
    print(f"환경 변수 PATH 일부: {':'.join(path_env.split(os.pathsep)[:3])}")
else:
    print("환경 변수 PATH를 찾을 수 없습니다.")


print("파일 경로 정보:")
file_path = "/Users/username/documents/report.txt"
print(f"- 디렉토리: {os.path.dirname(file_path)}")
print(f"- 파일명: {os.path.basename(file_path)}")
print(f"- 확장자: {os.path.splitext(file_path)[1]}")

# 파일 존재 여부 (예시 경로이므로 False가 나올 가능성이 높음)
print(f"파일 존재 여부: {os.path.exists(file_path)}")