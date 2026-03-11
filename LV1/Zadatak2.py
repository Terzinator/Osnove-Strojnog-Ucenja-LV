
while(True):
    print("Input percent of points (0.0 to 1.0): ")
    try:
        percentage = float(input())
    except:
        print("You did not enter a number")
    else:
        break


if(percentage<0 or percentage>1):
    print("Not a valid percentage")

else:
    if(percentage>=0.9):
        print("A")
    elif(percentage>=0.8):
        print("B")
    elif(percentage>=0.7):
        print("C")
    elif(percentage>=0.6):
        print("D")
    else:
        print("F")
