import sys
from collections import deque

maps = []
dx = [0,0,-1,1]
dy = [-1,1,0,0]
max_value = 0

def bfs():
    global max_value
    temp = [[0] * m for _ in range(n)]                      # 벽 3개를 세우는 모든 경우의 수에 대해 확인해봐야 하므로 맵 복사해서  진행
    for i in range(n):
        for j in range(m):
            temp[i][j] = maps[i][j]
    result = 0
    queue = deque()
    for i in range(n):                                      # 바이러스 있는 지점 큐에 삽입
        for j in range(m):
            if temp[i][j] == 2:
                queue.append((i,j))
    while queue:                                            # 바이러스 퍼트리기 시작
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx and nx < n and 0 <= ny and ny < m and temp[nx][ny] == 0:
                temp[nx][ny] = 2
                queue.append((nx,ny))

    for i in temp:                                          # 복사본에서 안전 구역 카운트
        for j in i:
            if j == 0:
                result += 1
    max_value = max(max_value, result)


def wall(cnt):                          # 벽 3개 선택
    if cnt == 3:
        bfs()
        return
    else:
        for i in range(n):
            for j in range(m):
                if maps[i][j] == 0:
                    maps[i][j] = 1
                    wall(cnt+1)
                    maps[i][j] = 0

n,m = map(int, sys.stdin.readline().split())    # 세로, 가로

for _ in range(n):
    maps.append(list(map(int, sys.stdin.readline().split())))
wall(0)
print(max_value)
