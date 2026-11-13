
s = list(map(int,input().split()))
k, c = map(int,input().split())

s[k:k] = [c]
print(*s)