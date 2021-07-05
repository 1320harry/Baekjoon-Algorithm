n,k = map(int,input().split())
data =[]
for i in range(n):
    data.append(int(input()))

data.sort(reverse=True)

count = 0 # 코인 개수
for i in range(n):
    if data[i]<=k:
        count+=(k//data[i])
        k=(k%data[i])
        if(k==0):
            break
print(count)

