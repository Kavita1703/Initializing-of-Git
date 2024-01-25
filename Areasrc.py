def sphere(r):
    Area=4*3.14*r*r
    print("Area of Sphere:",Area)


def rectangle(l,b):
    Area=l*b
    print("Area of Rectangle:",Area)


def cylinder(r,h):
    Area=2*3.14*r*(r+h) 
    print("Area of cylinder:",Area)
def menu():
    print (" enter 1 for area of sphere")
    print (" enter 2 for area of rectangle")
    print (" enter 3 for area of cylinder")
    num=int(input())
    if num==1:
        r=int(input("Enter radius of sphere:"))
        sphere(r)
    elif num==2:
        l=int(input("Enter length of rectangle:"))
        b=int(input("Enter breadth of rectangle:"))
        rectangle(l,b)
        
    
    elif num==3:
        r=int(input("Enter radius of cylinder:"))
        h=int(input("Enter height of cylinder:"))
        cylinder(r,h)
         
    else:
        print("invalid")
menu()







