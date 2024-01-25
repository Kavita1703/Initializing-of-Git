num=int(input("Enter any three digit Numbers:"))
temp=num
if(num>=100 and num<1000):
    f=num%10
    num=num//10
    s=num%10
    num=num//10
    t=num%10
    sum=f*f*f+s*s*s+t*t*t
    if(temp==sum):
        print("Armstrong no.")
    else:
        print("NOt Armstrong No.")
else:
    print("Entered no. is not 3 digits")
