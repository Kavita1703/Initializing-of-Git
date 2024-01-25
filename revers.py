num=int(input("Enter any three digit Numbers:"))
t=num%10
num=num//10
s=int(num%10)
f=int(num//10)
sum=(1*f+10*s+100*t)
print("Reverse of the number is:",int(sum))
