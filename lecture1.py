import math
a=int(input("Please enter a number(a): "))
b=int(input("Please enter a number(b): "))
A=float(input("Please enter a number(A): "))
if (-1)<=A<= 1 :
    c=math.sqrt((a*a)+(b*b)-(2*a*b*math.cos(A))) 
    print("Nice: ", c)
else:
    print("SOS!!!")