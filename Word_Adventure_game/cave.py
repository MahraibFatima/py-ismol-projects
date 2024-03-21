import forest

def enter_cave():
    print("You are in a mysterious cave.")
    action = input("What do you want to do? (explore/leave) ").lower()
    if action == "explore":
        print("You find a sleeping dragon! You're runing back to where you started.")
        forest.in_forest()
    elif action == "leave":
        print("You decide to leave the cave.")
        forest.in_forest()
    else:
        print("Invalid action. Please choose again.")
        enter_cave()
