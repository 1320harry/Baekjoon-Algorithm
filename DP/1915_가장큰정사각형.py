import sys
matrix = tuple(int(x) for x in sys.stdin.readline().split())
map=[list(map(int,sys.stdin.readline().rstrip())) for _ in range(matrix[0])]
dir = [(0,-1),(-1,-1),(-1,0)]


# 예외 처리 줄이기 위해, 0으로 둘러싼다.
map.insert(0,[0 for _ in range(matrix[1]+2)] )
map.insert(matrix[0]+1,[0 for _ in range(matrix[1]+2)])
for i in range(1,matrix[0]+1):
    map[i].insert(0,0)
    map[i].insert(matrix[1]+1,0)

largest = 0
for i in range(1,matrix[0]+1):
    for j in range(1,matrix[1]+1):
        if(map[i][j]==1):
            smallest = map[i+dir[0][0]][j+dir[0][1]]
            for k in dir:
                if map[i+k[0]][j+k[1]]<smallest:
                    smallest = map[i+k[0]][j+k[1]]
            map[i][j]+=smallest
            if map[i][j]>largest:
                largest = map[i][j]
print(largest**2)