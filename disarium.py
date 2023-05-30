
## Given Number is Disarium Number or not??

n=int(input("Enter the value: "))
num=n
sum=0
l=len(str(n))
while n>0:
    rem=n%10
    sum=sum+rem**l
    n=n//10
    l-=1
if sum==num:
    print("Disarium Number")
else:
    print("Not Disarium Number")
