*def red(r,b):
    print("VOILET color")
def blue(b,g):
    print("CYAN color")
def green(r,g):
    print("yellow")

    
def colors():
    print (" enter 1 for combination of RED and BLUE color")
    print (" enter 2 for combination of BLUE and GREEN color")
    print (" enter 3 for combination of RED and GREEN color")
    num=int(input())
    if num==1:
        red()
    elif num==2:
        b=input("Enter any color:")
        g=input("Enter color:")
        blue(b,g)
        
    
    elif num==3:
        r=input("Enter color:")
        g=input("Enter color:")
        green(r,g)
         
    else:
        print("invalid")
colors()


    
    
