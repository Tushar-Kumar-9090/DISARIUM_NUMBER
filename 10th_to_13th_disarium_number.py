
## WAP to print 10th to 13th disarium number

n=1
c=0
ll=int(input("Enter lower level number: "))
ul=int(input("Enter lower upper number: "))
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
        if c>=ll:
            print(n)
    if c==ul:
        break
    n+=1