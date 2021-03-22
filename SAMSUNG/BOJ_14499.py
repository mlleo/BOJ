import sys

def copy(x,y):
    if maps[x][y] == 0:
        maps[x][y] = dice[6]
    else:
        dice[6] = maps[x][y]
        maps[x][y] = 0

n, m, x, y, k = map(int, sys.stdin.readline().split())  # 세로, 가로, 주사위 좌표 x,y, 명령 개수
maps = []

for _ in range(n):
    maps.append(list(map(int, sys.stdin.readline().split())))

command = list(map(int, sys.stdin.readline().split()))

dice = [0] * 7

for com in command:  # 명령 반복하면서
    if com == 1:  # 동쪽
        # print("1번=================================================")
        if y == m - 1:  # 갈 수 없는 경우
            continue
        else:
            tmp = dice[1]
            dice[1] = dice[3]
            dice[3] = dice[6]
            dice[6] = dice[4]
            dice[4] = tmp
            y += 1
            copy(x,y)
    elif com == 2:  # 서쪽
        # print("2번=================================================")
        if y == 0:  # 갈 수 없는 경우
            continue
        else:
            tmp = dice[4]
            dice[4] = dice[6]
            dice[6] = dice[3]
            dice[3] = dice[1]
            dice[1] = tmp
            y -= 1
            copy(x,y)
    elif com == 3:  # 북쪽
        # print("3번=================================================")
        if x == 0:  # 갈 수 없는 경우
            continue
        else:
            tmp = dice[2]
            dice[2] = dice[1]
            dice[1] = dice[5]
            dice[5] = dice[6]
            dice[6] = tmp
            x -= 1
            copy(x,y)
    elif com == 4:  # 남쪽
        # print("4번=================================================")
        if x == n - 1:  # 갈 수 없는 경우
            continue
        else:
            tmp = dice[2]
            dice[2] = dice[6]
            dice[6] = dice[5]
            dice[5] = dice[1]
            dice[1] = tmp
            x += 1
            copy(x, y)

    print(dice[1])  # 가장 윗면 출력
