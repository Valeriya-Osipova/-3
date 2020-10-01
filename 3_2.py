a = []
b = 0
print("введите количество переменных массива")
n = int(input())
for i in range(0,n):
    a.append(int(input()))
    b = b+a[i]
b = b/len(a)
print(b)