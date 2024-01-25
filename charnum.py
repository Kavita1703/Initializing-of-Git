print("Enter any number or character")
a=input()
if(ord(a)>=65 and ord(a)<91) or (ord(a)>=97 and ord(a)<=122):
    print("It is an character")
elif(ord(a)>=47 and ord(a)<57):
    print("It is an number")
else:
    print("wrong input")
