import sys
N = int(sys.stdin.readline())
list=[]
dp=[[0 for _ in range(N)] for _ in range(N)]
for _ in range(N):
    row,col = map(int,sys.stdin.readline().split())
    list.append((row,col))

# N=1 일때는 0 으로 이미 정했음.
# N>=2 일 때 다음과 같이 일반화 가능
for i in reversed(range(N-1)): # reversed 넣어주는 것이 중요. 부분에서 전체로 계산해주니까
    for j in range(i+1,N):
        smallest = dp[i][i]+dp[i+1][j]+list[i][0]*list[i][1]*list[j][1]
        for k in range(i,j):
            cand=dp[i][k]+dp[k+1][j]+list[i][0]*list[k][1]*list[j][1]
            if cand <smallest:
                smallest = cand
        dp[i][j] = smallest

print(dp[0][N-1])

