import sys
n,k = map(int,sys.stdin.readline().split())
combi = [[0]*(n) for _ in range(n)]


for i in range(n):
    combi[i][0] = 1
    combi[i][i] = 1
    j=1
    while(j>0 and j<i):
        combi[i][j] = combi[i-1][j-1]+combi[i-1][j]
        j=j+1

print(combi[n-1][k-1])