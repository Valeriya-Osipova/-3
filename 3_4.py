a = []
m = int(input())
n = int(input())
for x in range (0,m):
    a.append([x**y for y in range (0,n)])
print(a)
