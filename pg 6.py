print('Celcius\t\t\tFarhenhiet')
for celcius in range(21):
    print(f'{celcius}\t\t\t',end='')
    f=int((9/5)*(celcius)+32)
    print(f,)
