s = input().split()
v = s[-1]
s.pop(-1)
s.insert(0,v)
print(*s)