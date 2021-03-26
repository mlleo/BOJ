import sys
from collections import deque

N, L, R = map(int, sys.stdin.readline().split())  # 맵 크기 n*n, 인구차이 L명 이상 R명 이하
maps = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]  # 각 나라별 인구는 최소 0명 최대 100명

def bfs(i,j):
    queue = deque()
    queue.append((i,j))
    temp = []
    temp.append((i,j))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                if L <= abs(maps[nx][ny] - maps[x][y]) <= R:
                    visited[nx][ny] = 1
                    queue.append((nx,ny))
                    temp.append((nx,ny))
    return temp


count = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

while True:
    visited = [[0] * N for _ in range(N)]
    flag = False
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:          # 방문하지 않은 국가가 있다면
                visited[i][j] = 1           # 방문
                temp = bfs(i,j)             # 해당 국가로부터 갈 수 있는 국가 계산
                if len(temp) > 1:
                    flag = True
                    num = sum(maps[x][y] for x,y in temp) // len(temp)
                    for x,y in temp:
                        maps[x][y] = num
    if not flag:
        break
    count += 1

print(count)
