year=int(input('Enter years:'))
i=1
month=0
inches_of_rainfall=0
while(i<=year):
    print(f'year {i}:')
    for j in range(1,13):
        rainfall=int(input(f'inches of rain fall for month {j}:'))
        inches_of_rainfall=inches_of_rainfall+rainfall

    i=i+1
a=year*12
print('Month:',a)
print('total inches of rainfall:',inches_of_rainfall)
print('average of rain fall per month:',inches_of_rainfall/a)
        
        
