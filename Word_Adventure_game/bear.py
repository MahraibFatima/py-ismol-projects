import random
import forest

def encounter_bear():
    print("You encounter a bear!")
    choice = input("Do you want to fight or run? (fight/run) ").lower()

    if choice == "fight":
        print("You decide to fight the bear...")
        if random.choice([True, False]):
            print("You fought valiantly but unfortunately, the bear was too strong. You are mauled to death.")
            print("You wake up in a cold sweat. It was all just a bad dream...")
            forest.in_forest()
        else:
            print("You managed to defeat the bear! You continue on your journey.")
            forest.in_forest()

    elif choice == "run":
        print("You decide to run back to where you started.")
        forest.in_forest()
        
    else:
        print("Invalid choice. Please choose again.")
        encounter_bear()
