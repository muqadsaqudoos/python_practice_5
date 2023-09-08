n=int(input('N:'))
for i in range(n):
    print(end='#')
    for j in range(i):
        if(j<i):
            print(end=' ')
    print(end='#')
    print()
