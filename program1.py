def additiom(a,b):
    return a+b
def subtraction(a,b):
    return a-b
def multiplcation(a,b):
    return a*b
def division(a,b):
    return a/b

n=int(input("enter the operation -\n"
            "1. Addition\n"
            "2. Subtraction\n"
            "3. Multiplication\n"
            "4. Division\n"
            ))

a=int(input("enter the first number"))
b=int(input("enter the second number"))
if n==1:
    print(additiom(a,b))
elif n==2:
    print(subtraction(a, b))
elif n==3:
    print(multiplcation(a, b))
elif n==4:
    print(division(a, b))
else:
    print("invalid")




