import random

def introduction():
    print("Welcome to the Text Adventure Game!")
    print("You find yourself in a mysterious house. Explore and see what you can find.")

def choose_action():
    print("What would you like to do?")
    print("1. Go left")
    print("2. Go right")
    print("3. Go straight")
    return input("Enter your choice (1, 2, or 3): ")

def encounter_monster():
    print("Oh no! A wild monster appears!")
    print("What will you do?")
    print("1. Fight")
    print("2. Run away")
    return input("Enter your choice (1 or 2): ")

def explore_room():
    print("You enter a room and look around.")
    choice = choose_action()

    if choice == "1":
        print("You go left and find a treasure chest!")
    elif choice == "2":
        decision = encounter_monster()
        if decision == "1":
            if random.choice([True, False]):
                print("You defeated the monster and found a key!")
            else:
                print("The monster was too strong. Game over!")
                return False
        elif decision == "2":
            print("You run away from the monster.")
    elif choice == "3":
        print("You go straight and find a mysterious portal.")

    return True

def main():
    introduction()
    
    while True:
        continue_playing = explore_room()

        if not continue_playing:
            break

    print("Thanks for playing!")

if __name__ == "__main__":
    main()
