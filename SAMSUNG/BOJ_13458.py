import sys

n = int(sys.stdin.readline())   # 시험장 개수
stu = list(map(int, sys.stdin.readline().split()))  # 시험장 별 응시생 수
b, c = map(int, sys.stdin.readline().split())   # 총감독, 부감독 감시 가능 수
count = 0

for students in stu:
    count += 1              # 총감독 1명 기본
    if students <= b:       # 총감독 혼자 커버 가능
        continue
    students -= b
    count += (students // c)    # 부감독 수 증가

    if students % c != 0:       # 나누어 떨어지지 않으면 부감독 한 명 추가
        count += 1

print(count)
