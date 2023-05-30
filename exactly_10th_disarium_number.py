
## WAP to print 10th disarium number

t=int(input("Enter which place disarium number you want:  "))
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
    if c==t:
        print(n)
        break
    n+=1
