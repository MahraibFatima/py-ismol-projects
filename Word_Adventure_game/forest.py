import random
import bear
import cave

def in_forest(has_key=False):
    print("You are in the dark forest.")
    direction = input("Which direction do you want to go? (north/south/east/west) ").lower()

    if direction == "north":
        print("You encounter a river. You cannot cross it.")
        print("You're going back to where you started.")
        in_forest(has_key)

    elif direction == "south":
        bear.encounter_bear()

    elif direction == "east":
        if has_key:
            print("You find a locked door. You use the key to unlock it!")
            print("Congratulations! You found teasure!")
        else:
            print("You find a clearing with a treasure chest!")
            print("You open the chest and find a key inside.")
            in_forest(True)

    elif direction == "west":
        print("You find a mysterious cave.")
        cave.enter_cave()
        
    else:
        print("Invalid direction. Please choose again.")
        in_forest(has_key)
