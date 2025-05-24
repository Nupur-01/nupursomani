n=int(input("enter the number"))
result=""
for i in range(1,n):
        x=2*i-1
        result=result+str(x)
        if i<n-1:
            result=result+","
        print(result)