def add():
        a=int(input("Enter 1st number:"))
        b=int(input("Enter 2nd number:"))
        add=a+b
        print("Addition:",add)
def subtract():
        a=int(input("Enter 1st number:"))
        b=int(input("Enter 2nd number:"))
        subs=a-b
        print("substraction",subs)
def multiply():
          a=int(input("Enter 1st number:"))
          b=int(input("Enter 2nd number:"))
          muly=a*b
          print("Multiplication:",muly)
def divide():
        a=int(input("Enter 1st number:"))
        b=int(input("Enter 2nd number:"))
        divide=a/b
        print("Divide:",divide)
        if b == 0:
            return "Error: Cannot divide by zero"
        return a / b
print ("1 for addition of two numbers")
print ("2 for substraction of two numbers")
print ("3 for  multiplication of two numbers")
print ("4 for division of two numbers")
print("enter yuor choice\n")
a=int(input())
if a==1:
    add()
elif a==2:
    subtract()
elif a==3:
    multiply()
elif a==4:
    divide()
else:
  print("invalid no.")
       

       
    

