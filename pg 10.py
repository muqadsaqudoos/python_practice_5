fact=int(input('number you want to take factorial:'))
sum=0
if(fact==1):
    print('1')
elif(fact==0):
    print('1')
else:
    for i in range(1,fact):
        fact=fact*i
    print(fact)
    
