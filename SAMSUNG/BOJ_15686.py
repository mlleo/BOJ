import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())               # 맵 크기 n*n, 치킨집 최대 개수 m
maps = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

chicken = []            # 치킨집
for i in range(n):
    for j in range(n):
        if maps[i][j] == 2:
            chicken.append([i,j])
            maps[i][j] = 0              # 빈 칸으로 수정

chicken_comb = list(combinations(chicken,m))      # 치킨 집 n개를 고르는 조합

min_value = sys.maxsize
for i in range(len(chicken_comb)):
    distance = 0
    for a in range(n):
        for b in range(n):
            if maps[a][b] == 1:
                temp = sys.maxsize
                for j in range(m):
                    temp = min(temp, abs(a-chicken_comb[i][j][0]) + abs(b-chicken_comb[i][j][1]))
                distance += temp
    min_value = min(min_value,distance)

print(min_value)
