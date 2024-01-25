num=int(input("Enter any three digit Numbers:"))
temp=num
if(num>=100 and num<1000):
    t=num%10
    num=num//10
    s=int(num%10)
    f=int(num//10)
    sum=(1*f+10*s+100*t)
    if(temp==sum):
        print("palindrome")
    else:
        print("Not palindrome")
else:
    print("entered no. is not three digits")

