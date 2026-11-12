s = list(map(int,input().split()))
s2 = int(input())
v1 = []
for i in s:
    if i >= s2:
        v1.append(i)

print(len(v1)+1)