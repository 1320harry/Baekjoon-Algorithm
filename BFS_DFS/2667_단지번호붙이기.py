import sys
N = int(sys.stdin.readline())
map = [list(map(int,sys.stdin.readline().rstrip())) for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]
list =[]

def dfs(x,y):
    global count
    if x<=-1 or x>=N or y<=-1 or y>=N:
        return count,False
    if map[x][y] == 1 and visited[x][y] == 0:
        visited[x][y] =1
        count+=1
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return count,True
    return count,False

for i in range(N):
    for j in range(N):
        count = 0
        num, tf = dfs(i,j)
        if tf == True:
            list.append(num)
list.sort()
print(len(list))
for i in list:
    print(i)
