import sys
num = int(sys.stdin.readline())
list = []
dp = [1 for _ in range(num)]
for _ in range(num):
    m =tuple(int(x) for x in sys.stdin.readline().split())
    list.append(m)
list.sort(key=lambda x:x[0])

largest_1 = dp[0]
for i in range(len(list)):
    largest_2 = 0
    for j in reversed(range(i)):
        if list[j][1]<list[i][1]:
            if dp[j]>largest_2:
                largest_2 = dp[j]
    dp[i]+=largest_2
    if dp[i]>largest_1:
        largest_1 = dp[i]

print(num-largest_1)
