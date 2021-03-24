import sys
from itertools import permutations

n = int(sys.stdin.readline())       # 수 개수
nums = list(map(int, sys.stdin.readline().split()))     # 숫자 입력

max_value = -1000000001
min_value = 1000000001

plus, minus, mul, div = map(int, sys.stdin.readline().split())  # 연산자 개수
opt = []                                                        # 연산자 리스트 

opt += ["+"] * plus
opt += ["-"] * minus
opt += ["*"] * mul
opt += ["/"] * div

opt_set = []

for opt_perm in list(permutations(opt)):
    opt_set.append(opt_perm)
opt_set = list(set(opt_set))                                        # 중복 제거

for case in opt_set:
    result = nums[0]

    for i in range(n-1):
        if case[i] == "+":
            result += nums[i+1]
        elif case[i] == "-":
            result -= nums[i+1]
        elif case[i] == "*":
            result *= nums[i+1]
        elif case[i] == "/":
            if result < 0:                          # 음수를 양수로 나누는 경우
                result = (abs(result) // nums[i+1]) * (-1)
            else:
                result //= nums[i+1]

    max_value = max(max_value,result)
    min_value = min(min_value, result)

print(max_value)
print(min_value)
