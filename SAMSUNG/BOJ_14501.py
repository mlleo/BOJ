import sys

n = int(sys.stdin.readline())   # 남은 일 수
t = []
p = []
memo = [0] * (n+1)

for _ in range(n):
    a,b = map(int, sys.stdin.readline().split())
    t.append(a)
    p.append(b)

# memo[i]는 i번째 날부터 시작해서 얻을 수 있는 최대 이익
for i in range(n-1,-1,-1):                  # 거꾸로 확인
    if t[i] + i > n:                        # 당일에 할당된 일을 하면 시간초과되는 경우
        memo[i] = memo[i+1]                 
    else:                                   # 당일에 할당된 일을 할 수 있는 경우
        memo[i] = max(memo[i+1], p[i]+memo[i+t[i]])

print(memo[0])
