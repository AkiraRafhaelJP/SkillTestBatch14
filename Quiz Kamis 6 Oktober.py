check = False

for i in range(1, 16):  
    if i % 3 == 0:
        print('fizz', end='')
        check = True

    if i % 5 == 0:
        print('buzz', end='')
        check = True
    
    if check:
        check = False
        print()
        continue

    print(i)