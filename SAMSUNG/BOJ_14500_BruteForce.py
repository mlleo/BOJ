import sys

n, m = map(int, sys.stdin.readline().split())   # 세로, 가로
maps = []                                       # 맵 정보
for i in range(n):
    maps.append(list(map(int, sys.stdin.readline().split())))

max_value = -1

# case 1
for i in range(n):
    for j in range(m-3):
        total = 0
        total += maps[i][j]
        total += maps[i][j+1]
        total += maps[i][j+2]
        total += maps[i][j+3]
        max_value = max(max_value,total)

for i in range(n-3):
    for j in range(m):
        total = 0
        total += maps[i][j]
        total += maps[i+1][j]
        total += maps[i+2][j]
        total += maps[i+3][j]
        max_value = max(max_value, total)

# case 2
for i in range(n-1):
    for j in range(m-1):
        total = 0
        total += maps[i][j]
        total += maps[i][j+1]
        total += maps[i+1][j]
        total += maps[i+1][j+1]
        max_value = max(max_value, total)

# case 3
for i in range(n-2):
    for j in range(m-1):
        total = 0
        total += maps[i][j]
        total += maps[i+1][j]
        total += maps[i+2][j]
        total += maps[i+2][j+1]
        max_value = max(max_value, total)

for i in range(n-1):
    for j in range(m-2):
        total = 0
        total += maps[i][j]
        total += maps[i+1][j]
        total += maps[i][j+1]
        total += maps[i][j+2]
        max_value = max(max_value, total)

for i in range(n-2):
    for j in range(m-1):
        total = 0
        total += maps[i][j]
        total += maps[i][j+1]
        total += maps[i+1][j+1]
        total += maps[i+2][j+1]
        max_value = max(max_value, total)

for i in range(n-1):
    for j in range(m-2):
        total = 0
        total += maps[i+1][j]
        total += maps[i+1][j+1]
        total += maps[i][j+2]
        total += maps[i+1][j+2]
        max_value = max(max_value, total)

for i in range(n-2):
    for j in range(m-1):
        total = 0
        total += maps[i][j]
        total += maps[i][j+1]
        total += maps[i+1][j]
        total += maps[i+2][j]
        max_value = max(max_value, total)

for i in range(n-2):
    for j in range(m-1):
        total = 0
        total += maps[i][j+1]
        total += maps[i+1][j+1]
        total += maps[i+2][j]
        total += maps[i+2][j+1]
        max_value = max(max_value, total)

for i in range(n-1):
    for j in range(m-2):
        total = 0
        total += maps[i][j]
        total += maps[i][j+1]
        total += maps[i][j+2]
        total += maps[i+1][j+2]
        max_value = max(max_value, total)

for i in range(n-1):
    for j in range(m-2):
        total = 0
        total += maps[i][j]
        total += maps[i+1][j]
        total += maps[i+1][j+1]
        total += maps[i+1][j+2]
        max_value = max(max_value, total)

# case 4
for i in range(n-2):
    for j in range(m-1):
        total = 0
        total += maps[i][j]
        total += maps[i+1][j]
        total += maps[i+1][j+1]
        total += maps[i+2][j+1]
        max_value = max(max_value, total)

for i in range(n-1):
    for j in range(m-2):
        total = 0
        total += maps[i][j+1]
        total += maps[i][j+2]
        total += maps[i+1][j]
        total += maps[i+1][j+1]
        max_value = max(max_value, total)

for i in range(n-2):
    for j in range(m-1):
        total = 0
        total += maps[i][j+1]
        total += maps[i+1][j]
        total += maps[i+1][j+1]
        total += maps[i+2][j]
        max_value = max(max_value, total)

for i in range(n-1):
    for j in range(m-2):
        total = 0
        total += maps[i][j]
        total += maps[i][j+1]
        total += maps[i+1][j+1]
        total += maps[i+1][j+2]
        max_value = max(max_value, total)

# case 5
for i in range(n-1):
    for j in range(m-2):
        total = 0
        total += maps[i][j+1]
        total += maps[i+1][j]
        total += maps[i+1][j+1]
        total += maps[i+1][j+2]
        max_value = max(max_value, total)

for i in range(n-1):
    for j in range(m-2):
        total = 0
        total += maps[i][j]
        total += maps[i][j+1]
        total += maps[i][j+2]
        total += maps[i+1][j+1]
        max_value = max(max_value, total)

for i in range(n-2):
    for j in range(m-1):
        total = 0
        total += maps[i][j]
        total += maps[i+1][j]
        total += maps[i+1][j+1]
        total += maps[i+2][j]
        max_value = max(max_value, total)

for i in range(n-2):
    for j in range(m-1):
        total = 0
        total += maps[i][j+1]
        total += maps[i+1][j]
        total += maps[i+1][j+1]
        total += maps[i+2][j+1]
        max_value = max(max_value, total)

print(max_value)
