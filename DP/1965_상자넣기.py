import sys
box = int(sys.stdin.readline())
order = list(map(int,sys.stdin.readline().split() ) )
dp = [1 for _ in range(box)]


largest_1 = dp[0]
for i in range(0,box):
    largest_2 = 0
    for j in reversed(range(i)):
        if order[j] < order[i]:
            if dp[j]>largest_2:
                largest_2 =dp[j]
    dp[i]+=largest_2
    if dp[i]>largest_1:
        largest_1 = dp[i]

print(largest_1)