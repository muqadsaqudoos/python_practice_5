speed=int(input('speed in mph:'))
time=int(input('time in hour:'))
i=1
while(i<=time):
    distance=i*speed
    print(f'distance in {i} hour:{distance}')
    i+=1
