s = input().split()
print(*next(([s[i-1], s[i]] for i in range(1, len(s)) if int(s[i]) * int(s[i-1]) > 0), []))