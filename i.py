s = list(map(int, input().split()))
v = []
for i in s:
    if i % 2 != 0:
        v.append(i)

if len(v) == 0:
    print(0)
else:
    print(min(v))

