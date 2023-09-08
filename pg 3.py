n=int(input("Budget for month:"))
a=0
total=0
while a==0:
        b=int(input('Enter spend amount:'))
        total=total+b
        a=int(input('print 0 to countinue:'))
if(n>total):
    print('You are under budget')
elif(n==total):
    print('Equal budget')
else:
    print('you are over budget')
print(total)
