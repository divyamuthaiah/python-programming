n=int(input("Enter any number: "))
c=list(map(int,str(n)))
d=list(map(lambda x:x**3,c))
if(sum(d)==n):
       print("The number is an armstrong number. ")
else:
       print("The number isn't an arsmtrong number. ")
