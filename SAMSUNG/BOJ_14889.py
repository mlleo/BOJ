import sys
from itertools import combinations

n = int(sys.stdin.readline())       # 총 인원수
score = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
members = [i+1 for i in range(n)]
team_list = []

for team in list(combinations(members, n//2)):      # 가능한 팀 조합 계산
    team_list.append(team)

min_value = 10000

for i in range(len(team_list)//2):
    team_A = team_list[i]                 # 특정 팀 선택
    stat_A = 0
    for j in range(n//2):                 # 특정 맴버 선택
        member = team_A[j]
        for k in team_A:                  # 맴버로 인해 팀에 더해지는 능력치 계산
            stat_A += score[member-1][k-1]

    team_B = team_list[-i-1]              # 나머지 다른 팀도 같은 원리
    stat_B = 0
    for j in range(n//2):
        member = team_B[j]
        for k in team_B:
            stat_B += score[member-1][k-1]
    min_value = min(min_value, abs(stat_A-stat_B))

print(min_value)
