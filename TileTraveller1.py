herbergi11 = True
herbergi12 = False
herbergi13 = False
herbergi21 = False
herbergi22 = False
herbergi23 = False
herbergi31 = False
herbergi32 = False
herbergi33 = False

North = False
East = False
West = False
South = False

victory = False

while victory == False:
    while herbergi11 == True:
        North = True
        print("You can travel: (N)orth.")
            direction = input("Direction: ")
            if direction == "n" or direction == "N":
                herbergi11 = False
                herbergi12 = True
            else:
                print("Not a valid direction!")

    while herbergi12 == True:
        North = True
        South = True
        East = True
        print("You can travel: (N)orth or (E)ast or (S)outh.")
        direction = input("Direction: ")
        if direction == "n" or direction == "N":
            herbergi12 = False
            herbergi13 = True
        elif direction == "s" or direction == "S":
            herbergi12 = False
            herbergi11 = True
        elif direction == "e" or direction == "E":
            herbergi12 = False
            herbergi22 = True
        else:
            print("Not a valid direction!")
    
    while herbergi22 == True:
        West = True
        South = True
        print("You can travel: (S)outh or (W)est.")
        direction = input("Direction: ")
        if direction == "w" or direction == "W":
            herbergi22 = False
            herbergi12 = True
        elif direction == "s" or direction == "S":
            herbergi22 = False
            herbergi21 = True
        else:
            print("Not a valid direction!")

    while herbergi21 == True:
        North = True
        print("You can travel: (N)orth.")
        direction = input("Direction: ")
        if direction == "n" or direction == "N":
            herbergi21 = False
            herbergi22 = True
        else:
            print("Not a valid direction!")

    while herbergi13 == True:
        South = True
        East = True
        print("You can travel: (E)ast or (S)outh.")
        direction = input("Direction: ")
        if direction == "e" or direction == "E":
            herbergi13 = False
            herbergi23 = True
        elif direction == "s" or direction == "S":
            herbergi13 = False
            herbergi12 = True
        else:
            print("Not a valid direction!")

    while herbergi23 == True:
        East = True
        West = True
        print("You can travel: (E)ast or (W)est.")
        direction = input("Direction: ")
        if direction == "e" or direction == "E":
            herbergi23 = False
            herbergi33 = True
        elif direction == "w" or direction == "W":
            herbergi23 = False
            herbergi13 = True
        else:
            print("Not a valid direction!")

    while herbergi33 == True:
        South = True
        West = True
        print("You can travel: (S)outh or (W)est.")
        direction = input("Direction: ")
        if direction == "s" or direction == "S":
            herbergi33 = False
            herbergi32 = True
        elif direction == "w" or direction == "W":
            herbergi33 = False
            herbergi23 = True
        else:
            print("Not a valid direction!")

    while herbergi13 == True:
        South = True
        East = True
        print("You can travel: (E)ast or (S)outh.")
        direction = input("Direction: ")
        if direction == "e" or direction == "E":
            herbergi13 = False
            herbergi23 = True
        elif direction == "s" or direction == "S":
            herbergi13 = False
            herbergi12 = True
        else:
            print("Not a valid direction!")

    while herbergi32 == True:
        North = True
        South = True
        print("You can travel: (N)orth or (S)outh.")
        direction = input("Direction: ")
        if direction == "n" or direction == "N":
            herbergi32 = False
            herbergi33 = True
        elif direction == "s" or direction == "S":
            herbergi32 = False
            herbergi31 = True
        else:
            print("Not a valid direction!")

    if herbergi31 == True:
        victory = True

print("Victory!")
