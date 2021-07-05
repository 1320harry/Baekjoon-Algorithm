import sys
T = int(sys.stdin.readline())
combi = [[0]*30 for _ in range(30)]

for i in range(len(combi)):
    combi[i][0]= 1
    combi[i][i] = 1
    j=1
    while(j>0 and j<i):
        combi[i][j] = combi[i-1][j-1]+combi[i-1][j]
        j=j+1

for i in range(T):
    n,m = map(int,sys.stdin.readline().split())
    print(combi[m][n])




