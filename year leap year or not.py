year=int(input('enter the year:'))
if(year%4==0)
print('year is a leap year')
elif year%100==0:
print('year is not leap year')
elif year%400==0:
print('year is a leap year')
else:
print('year is not a leap year')
