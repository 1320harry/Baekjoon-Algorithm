import sys
n=int(input())
grape= [0]*(n+3)
dp = [0]*(n+3)
for i in range(n):
    grape[i] = int(sys.stdin.readline())

dp[0] = grape[0]
dp[1] = grape[0]+grape[1]
dp[2] = max(dp[1],max(grape[0],grape[1])+grape[2])

for i in range(n):
    dp[i+3] = max(dp[i+2],dp[i]+grape[i+2]+grape[i+3],dp[i+1]+grape[i+3])


print(dp[n-1])