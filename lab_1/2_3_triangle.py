
a = int(input("Введите кол-во ступенек: "))
for i in range(1, a+1):
    for j in range(1, i+1):

        print(j, end='')
    if i > 8:
        print()
        if i > 98:
            print()
    print()