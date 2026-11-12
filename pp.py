s = list(map(int,input().split()))
mx = max(s)
mn = min(s)
v = []
for i in s:
    if i == mx:
        i = mn
        v.append(i)
    elif i == mn:
        i = mx
        v.append(i)
    else:
        v.append(i)
print(*v)
