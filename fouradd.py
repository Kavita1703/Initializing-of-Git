num=int(input("Enter any four digit Numbers:"))
f=num%10
num=num//10
s=num%10
num=num//10
t=num%10
num=num//10
fth=num%10
sum=f+s+t+fth
print("Addition of digits:",int(sum))
