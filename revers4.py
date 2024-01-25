num=int(input("Enter any four digit Numbers:"))
fth=num%10
num=num//10
t=num%10
num=num//10
s=int(num%10)
f=int(num//10)
sum=(1*f+10*s+100*t+1000*fth)
print("Reverse of the number is:",int(sum))
