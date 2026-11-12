s = list(map(int, input().split()))
v =[]
for i in s:
    if i > 0:
        v.append(i)
print(min(v))