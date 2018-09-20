# Player starts in room 1.1 and needs to cross towards room 3.1 in a 3x3 maze with a few walls ahead
# In every room the choice of directions is prompted to the player and they will put the first letter
# to indicate their choice of direction.
# High and lower case letters are allowed but anything else will yield an error message
# Depending on the player's choice of direction, the current_room variable will change which indicates
# Their current position in the maze. For example, current_room starts in 1.1 and they can only move north.
# When North is selected, 1 will be added to the current_room variable to indicate that the player is now in
# room 1.2 and the code looks up what current_room will now give as choice of directions.
# This continues until the player reaches 3.1, in which the victory statement will become true and the loop ends.

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