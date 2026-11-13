s = list(map(int, input().split()))
v1 = 0
v = []
for i in range(len(s)):
    c = 0
    for j in range(len(s)):
        if s[i] == s[j]:
            c += 1
    if c > v1:
        v1 = c
        v = s[i]
print(v)

