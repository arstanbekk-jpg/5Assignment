s = input().split()
print(*[i for i in s if int(i) % 2 == 0])