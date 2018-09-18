valid_direction = "n"
victory = False
current_room = 11
print("You can travel: (N)orth.")

while not victory:
    direction = input("Direction: ")
    direction = direction.lower()
    if not direction in valid_direction:
        print("Not a valid direction!")
    else:
        if direction == "n":
            current_room += 1
        elif direction == "e":
            current_room += 10
        elif direction == "s":
            current_room -= 1
        else:
            current_room -= 10
    
        if current_room == 11:
            valid_direction = "n"
            print("You can travel: (N)orth.")
        elif current_room == 12:
            valid_direction = "n", "e", "s"
            print("You can travel: (N)orth or (E)ast or (S)outh.")
        elif current_room == 13:
            valid_direction = "e", "s"
            print("You can travel: (E)ast or (S)outh.")
        elif current_room == 22:
            valid_direction = "s", "w"
            print("You can travel: (S)outh or (W)est.")
        elif current_room == 21:
            valid_direction = "n"
            print("You can travel: (N)orth.")
        elif current_room == 23:
            valid_direction = "e", "w"
            print("You can travel: (E)ast or (W)est.")
        elif current_room == 33:
            valid_direction = "s", "w"
            print("You can travel: (S)outh or (W)est.")
        elif current_room == 32:
            valid_direction = "n", "s"
            print("You can travel: (N)orth or (S)outh.")
        else:
            victory = True
        
print("Victory!")