import sys
n = int(input())
stair = [0]*(n+4)
dp = [0]*(n+4)
for i in range(n):
    stair[i+1]= int(sys.stdin.readline())

dp[1] = stair[1]
dp[2] = stair[1]+stair[2]
for i in range(n+1):
    dp[i+3] = max(dp[i+1],dp[i]+stair[i+2]) + stair[i+3]
print(dp[n])

