a = str(input())
a = a.title()
x = a.index(' ') +1
y = a[x:]
y = y.index(' ') +1 + x
name = a[x:y]
name = name[0]+'. '
otch = a[y:]
otch = otch[0]+'. '
a = a[:x]
print(a+name+otch)
