a = [10, 2, 3, 44, 5, 256, 6, 7, 68]
b = []

for i in range(len(a)):
    for j in range(i+1, len(a)):
        if a[i] == a[j] and a[i] not in b:
            b.append(a[i])

if b:
    print("Повторяющиеся элементы:", b)
else:
    print("Нет повторяющихся чисел")




