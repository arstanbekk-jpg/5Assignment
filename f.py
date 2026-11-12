s = input().split()
print(len([i for i in range(1,len(s)-1) if int(s[i]) > int(s[i-1]) and int(s[i]) > int(s[i+1]) ]))