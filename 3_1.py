a = []
while True:
    try:
        number = float(input())
        a.append(number)
    except ValueError:
        break
print(len(a))