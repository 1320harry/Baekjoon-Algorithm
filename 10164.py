import sys
n,m,k = map(int,sys.stdin.readline().split())

combi = [[0]*30 for i in range(30)]

# print(combi[0])
# print(combi[29])

i=1
while(i>=1 and i<30):
    combi[i][0] =1
    combi[i][i] =1
    j=1
    while(j>0 and j<i):
        combi[i][j] = combi[i-1][j-1]+combi[i-1][j]
        j=j+1
    i=i+1


if(k%m != 0):
    x= k//m
    y = (k%m)-1
else:
    x = (k//m)-1
    y = m-1

if k!=0:
    total = (combi[x+y][y])*(combi[n-1-x+m-1-y][m-1-y])

if k==0:
    total = (combi[n-1+m-1][m-1])

print(total)
