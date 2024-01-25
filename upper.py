print("Enter any character:")
a=input()
if(ord(a)>=65 and ord(a)<91):
    b=ord(a)
    b=b+32
    print("lower case")
    print(chr(b))
if(ord(a)>=97 and ord(a)<=122):
        b=ord(a)
        b=b-32
        print("upper Case")
        print(chr(b))
