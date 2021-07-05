import sys
from collections import deque
total  = int(sys.stdin.readline())
p_1,p_2 = map(int, sys.stdin.readline().split())
rel = int(sys.stdin.readline())

fam = [[] for i in range(total+1)]
visited =[0]*(total+1)
for i in range(rel):
    x,y = map(int,sys.stdin.readline().split())
    fam[x].append(y)
    fam[y].append(x)


def bfs(graph, start, visited,target):
    queue = deque([start])
    visited[start] = 0
    while queue:
        v= queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = visited[v]+1
                if i == target:
                    break

bfs(fam,p_1,visited,p_2)
if visited[p_2] == 0:
    print(-1)
else:
    print(visited[p_2])
