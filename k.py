s = list(map(int,input().split()))
v = []
for i in s:
    if i not in v:
        v.append(i)
print(len(v))