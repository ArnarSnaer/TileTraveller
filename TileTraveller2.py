def dir_check(x):
    dir_okay = False
    direction = input("Direction: ")
    direction = direction.lower()
    if not direction in x:
        return dir_okay, direction
    else:
        dir_okay = True
        return dir_okay, direction

def number_change(y, z):
    if y == "n":
        z += 1
    elif y == "e":
        z += 10
    elif y == "s":
        z -= 1
    else:
        z -= 10
    return z

def new_directions(xa):
    valid_direction = ""
    if xa == 11:
        valid_direction = "n"
        print("You can travel: (N)orth.")
        return valid_direction, False
    elif xa == 12:
        valid_direction = "n", "e", "s"
        print("You can travel: (N)orth or (E)ast or (S)outh.")
        return valid_direction, False
    elif xa == 13:
        valid_direction = "e", "s"
        print("You can travel: (E)ast or (S)outh.")
        return valid_direction, False
    elif xa == 22:
        valid_direction = "s", "w"
        print("You can travel: (S)outh or (W)est.")
        return valid_direction, False
    elif xa == 21:
        valid_direction = "n"
        print("You can travel: (N)orth.")
        return valid_direction, False
    elif xa == 23:
        valid_direction = "e", "w"
        print("You can travel: (E)ast or (W)est.")
        return valid_direction, False
    elif xa == 33:
        valid_direction = "s", "w"
        print("You can travel: (S)outh or (W)est.")
        return valid_direction, False
    elif xa == 32:
        valid_direction = "n", "s"
        print("You can travel: (N)orth or (S)outh.")
        return valid_direction, False
    else:
        valid_direction = ""
        return valid_direction, True

valid_direction = "n"
victory = False
current_room = 11
print("You can travel: (N)orth.")

while not victory:
    direction_check, direction = dir_check(valid_direction)
    if direction_check == False:
        print("Not a valid direction!")
    else:
        current_room = number_change(direction, current_room)
        valid_direction, victory = new_directions(current_room)

print("Victory!")