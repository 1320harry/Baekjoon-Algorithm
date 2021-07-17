import sys
from collections import deque
width,depth,height = map(int,sys.stdin.readline().split())
tomato = [[[-1 for _ in range(width+2)] for _ in range(depth+2)] for _ in range(height+2)]
visited = [[[False for _ in range(width+2)] for _ in range(depth+2)] for _ in range(height+2)]
dir =[(0,0,-1),(0,0,1),(0,-1,0),(0,1,0),(-1,0,0),(1,0,0)] # 왼쪽, 오른쪽, 뒤, 앞, 아래,위

for i in range(1,height+1):
    for j in range(1,depth+1):
        tomato[i][j] = list(map(int,sys.stdin.readline().split()))
        tomato[i][j].insert(0,-1)
        tomato[i][j].insert(width+1,-1)

def bfs(graph,visited,count):
    queue = deque()
    list = []
    for i in range(1,height+1):
        for j in range(1,depth+1):
            for k in range(1,width+1):
                if tomato[i][j][k] == 1:
                    list.append((i,j,k))
                    visited[i][j][k] = True
                    continue
                elif tomato[i][j][k] == -1:
                    visited[i][j][k] = True
                    continue

    queue.append(list)
    while queue:
        list_1 = []
        list= queue.popleft()
        for v in list:
            for d in dir:
                if tomato[v[0]+d[0]][v[1]+d[1]][v[2]+d[2]]==0 and visited[v[0]+d[0]][v[1]+d[1]][v[2]+d[2]] ==False:
                    tomato[v[0] + d[0]][v[1] + d[1]][v[2] + d[2]] =1
                    list_1.append((v[0] + d[0],v[1] + d[1],v[2] + d[2]))
                    visited[v[0] + d[0]][v[1] + d[1]][v[2] + d[2]] =True
        if list_1:
            queue.append(list_1)
            count+=1
    for i in range(1, height + 1):
        for j in range(1, depth + 1):
            for k in range(1, width + 1):
                if tomato[i][j][k] == 0:
                    return -1
    return count

print(bfs(tomato,visited,0))







