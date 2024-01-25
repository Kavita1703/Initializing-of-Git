num=int(input("Enter any four digit Numbers:"))
if(num>=1000 and num<10000):
    temp=num
    f=num%10
    num=num//10
    s=num%10
    num=num//10
    t=num%10
    num=num//10
    fth=num%10
    sum=f*f*f*f+s*s*s*s+t*t*t*t+fth*fth*fth*fth
    if(temp==sum):
        print("Armstrong no.")
    else:
        print("Not Armstrong no.")
else:
    print("entered no. is not 4 digits")
