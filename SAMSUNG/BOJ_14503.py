import sys

n, m = map(int, sys.stdin.readline().split())    # 세로 ,가로
r, c, d = map(int, sys.stdin.readline().split())    # 현재 청소기 좌표 r,c, 방향 d(0:북, 1:동, 2: 남, 3: 서)
maps = []                                           # 맵 (0: 빈 칸, 1: 벽)
dr = [-1,0,1,0]
dc = [0,1,0,-1]
for _ in range(n):
    maps.append(list(map(int, sys.stdin.readline().split())))


def turn():                         # 회전
    global d
    d -= 1
    if d == -1:
        d = 3

maps[r][c] = 2              # 현재 위치 청소
count = 1

turn_count = 0

while True:
    turn()                      # 왼쪽으로 회전
    nr = r + dr[d]
    nc = c + dc[d]

    if maps[nr][nc] == 0:     # 이동할 장소가 청소가능하면
        maps[nr][nc] = 2      # 청소한 칸을 2로 지정
        r = nr
        c = nc
        count += 1
        turn_count = 0
        continue
    else:
        turn_count += 1

    if turn_count == 4:                 # 네 방향 모두 확인한 경우
        nr = r - dr[d]
        nc = c - dc[d]
        if maps[nr][nc] != 1:           # 뒤쪽이 벽이 아니면
            r = nr
            c = nc
        else:                           # 뒤쪽이 벽이면
            break
        turn_count = 0

print(count)
