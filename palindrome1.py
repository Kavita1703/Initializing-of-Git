num=int(input("Enter any four digit Numbers:"))
if(num>=1000 and num<10000):
    tem=num
    fth=num%10
    num=num//10
    t=num%10
    num=num//10
    s=int(num%10)
    f=int(num//10)
    sum=(1*f+10*s+100*t+1000*fth)
    if(tem==sum):
        print("palindrome")
    else:
        print("Not palindrome")
else:
    print("its not four digit")
