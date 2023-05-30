
## WAP to print first 10th disarium number
#! Dynamically

t=int(input("Enter how many disarium number you want: "))
n=1
c=0
while True:
    num=n
    sum=0
    l=len(str(n))
    while num>0:
        rem=num%10
        sum=sum+rem**l
        num=num//10
        l-=1
    if sum==n:
        c+=1
        print(n)
    if c==t:
        break
    n+=1