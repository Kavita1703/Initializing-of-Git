def color():
    print("BLACK")
def color(one):
    if(one=='r'):
        print("Red")
    elif(one=='b'):
        print("BLUE")
    elif(one=='g'):
        print("GREEN")
    else:
        print("pls entered invalid color")
def color(one,two):
    if((one=='red' and two=='blue') or (one=='blue' and two=='red')):
        print("Voilet")
    elif((one=='red' and two=='green') or (one=='green' and two=='red')):
        print("yellow")
    elif((one=='blue' and two=='green') or (one=='green' or two=='blue')):
        print("CYAN")
    elif(one=='red' and two=='red'):
        print("RED")
    elif(one=='blue' and two=='blue'):
        print("BLUE")
    elif(one=='green' and two=='green'):
        print("GREEN")
    else:
        print("plz enter valid pair")
def color(one,two,three):
    if((one=='red' and two=='blue' and three=='green') or (one=='blue' and two=='green' and three=='red')or(one=='green' and two=='red' and three=='blue')):
        print("WHITE")
    elif(one=='red' and two=='red' and three=='red'):
        print("RED")
    elif(one=='blue' and two=='blue' and three=='blue'):
        print("BLUE")
    elif(one=='green' and two=='green' and three=='green'):
        print("GREEN")
    elif((one=='red' and two=='red' and three=='blue') or (one=='blue' and two=='red' and three=='red') or (one=='red' and two=='blue' and three=='red')):
        print("VOILET")
    elif((one=='red' and two=='red' and three=='green') or (one=='green' and two=='red' and three=='red') or (one=='red' and two=='green' and three=='red')):
         print("Yellow")
    elif((one=='green' and two=='green' and three=='blue')or (one=='green' and two=='blue' and three=='green') or (one=='blue' and two=='green' and three=='green')):
        print("CYAN")
    elif((one=='blue' and two=='blue' and three=='red') or (one=='blue' and two=='red' and three=='blue') or (one=='red' and two=='blue' and three=='blue')):
        print("VOILET")
    elif((one=='blue' and two=='blue' and three=='green') or (one=='green' and two=='blue' and three=='blue') or (one=='blue' and two=='green' and three=='blue')):
         print("CYAN")
    elif((one=='green' and two=='green' and three=='red')or (one=='green' and two=='red' and three=='green') or (one=='red' and two=='green' and three=='green')):
        print("yellow")
    else:
        print("wrong input")
def menu():
    print("Enter 1 for single parameter:")
    print("Enter 2 for double parameter:")
    print("Enter 3 for triple parameter:")
    op=int(input("select any option"))
    if(op==1):
        color(one)
    elif(op==2):
        color(one,two)
    elif(op==3):
        color(one,two,three)
    else:
        color()
    
    



