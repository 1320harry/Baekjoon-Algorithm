import sys
from collections import deque
width, depth = map(int, sys.stdin.readline().split())
tomato = [[-1 for _ in range(width+2)] for _ in range(depth+2)]
visited = [[False for _ in range(width+2)] for _ in range(depth+2)]
dx = [0,0,-1,1]
dy = [-1,1,0,0]


for i in range(1,depth+1):
    tomato[i] = list(map(int,sys.stdin.readline().split()))
    tomato[i].insert(0,-1)
    tomato[i].insert(width+1,-1)

def bfs(graph,visited,count):
    list_1 = []
    queue = deque()
    for i in range(1,depth+1):
        for j in range(1,width+1):
            if tomato[i][j] == 1:
                list_1.append((i,j))
                visited[i][j] = True
                continue
            elif tomato[i][j] == -1:
                visited[i][j] = True
                continue
    queue.append(list_1)
    while queue:
        list_2 = []
        list = queue.popleft()
        for v in list:
            for i in range(4):
                if tomato[v[0]+dx[i]][v[1]+dy[i]] == 0 and visited[v[0]+dx[i]][v[1]+dy[i]] == False:
                    tomato[v[0]+dx[i]][v[1]+dy[i]] = 1
                    list_2.append((v[0]+dx[i],v[1]+dy[i]))
                    visited[v[0]+dx[i]][v[1]+dy[i]] = True

        if list_2:
            queue.append(list_2)
            count+=1
    for i in range(1, depth + 1):
        for j in range(1, width + 1):
            if tomato[i][j] == 0:
                return -1
    return count

print(bfs(tomato,visited,0))