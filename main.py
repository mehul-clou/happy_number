def happy_number(n):
    result=0
    while n>0:
        first_number = n%10
        result = result + (first_number*first_number)
        n=n//10
    return result


n=int(input("enter a number"))
result = n
while result!=1 and result!=4:
    result=happy_number(result)
if result==1:
    print(n,"is a happy number")
else:
    print(n,"is not a happy number")