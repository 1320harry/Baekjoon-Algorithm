import sys
N = int(sys.stdin.readline().rstrip())
dp = [0 for _ in range(N+1)]

if N<=3:
    if N==2:
        print("SK")
    else:
        print("CY")
else:
    dp[0] = 0
    dp[1] = 0
    dp[2] = 1
    dp[3] = 0

    for i in range(4,N+1):
        if dp[i-1] ==0 or dp[i-3] ==0 or dp[i-4] == 0:
            dp[i] = 1

    if dp[N]==1:
        print("SK")
    else:
        print("CY")
