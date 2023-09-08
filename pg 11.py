s=int(input('Starting number of organisms:'))
a=float(input('average daily increase:'))
n=int(input('Number of days to multiply:'))
print('Day approximate\t\tPopulation')
for i in range(1,n+1):
    print(f'{i}\t\t{s}')
    b=a*s
    s=s+b
