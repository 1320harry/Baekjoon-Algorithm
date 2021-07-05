import sys
sys.setrecursionlimit(10**6)
n,m = map(int,input().split())
pic = []
for i in range(n):
    pic.append( list( map( int,input().split() ) ) )
count = 0
area = 0


def dfs(x,y):

    global area


    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False

    if pic[x][y] == 1:
        area += 1
        pic[x][y] =0
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True
    return False


biggest = 0
for i in range(n):
    for j in range(m):
        area = 0
        if dfs(i,j) == True:
            if biggest < area:
                biggest = area
            count+=1

print(count)
print(biggest)