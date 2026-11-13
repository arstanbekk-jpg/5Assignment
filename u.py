s = list(map(int, input().split()))
c = 0
for i in range(len(s)):
    flag = True
    for j in range(i):
        if s[i] == s[j]:
            flag = False
            break
    if flag:
        c += 1
print(c)
