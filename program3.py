n=int(input("enter the number"))
if n%2==0:
    n=n-1

result=""
for i in range(n):
        x=2*i+1
        result=result+str(x)
        if i<n-1:
            result=result+","
print(result)