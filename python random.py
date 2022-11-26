#TO CHECK THE PROPERTIES OF A NUMBER RANDOMLY CHOOSEN
import random
lower_limit=int(input("enter the lower limit of range of numbers to be checked:",))
upper_limit=int(input("enter the upper limit of range of numbers to be checked:",))
x=random.randint(lower_limit,upper_limit)
print(x,"is the number randomly choosen by the user")
if x%2==0:
  print(x,"is an even number")
else:# x%2 is not 0:
  print(x,"is an odd number")
if x>0:
  print(x,"is a positive number")
else:#x<0:
  print(x,"is a negative number")
if x>1:
  for i in range(2,int(x/2)+1):
    if (x%i)==0:print(x,"is not a prime number")
    break
  else:
    print(x,"is a prime number")
