import time

def death(reason):
    print("{} | GG".format(reason))
    exit(0)

def guard():
    actions = {"check": "You see the guard is still asleep. You need to get to that door; What will you do?",
    "sneak":"You approach the guard, he's asleep. You reach for the door, and you open it slowly, you slip out.",
    "attack":"You swiftly run towards the sleeping guard and knock him out with the hilt of your sword, it wasn't hard enough. (heh, thats what she said)"}

    while True:
            action = input("What do you do? [Attack, Sneak] > ")
            
            if action.lower() in actions.keys():
                if action.lower() == "sneak":
                    print("You slip through the door and before the guard realised it, you were gone.")
                    print("Hooray, You're now free!")
                    return
                elif action.lower() == "attack":
                    death("The guard woke with a grunt, grabbed his dagger and stabbed you right through the chest.")

def left():
    loot = ["Diamonds", "Gold", "Silver", "Sword"]
    print("You find yourself in a room with a wooden chest on the left, and a sleeping guard on the right, in front of a door.")

    action = input("What do you do? [Chest, Guard] > ")

    if action.lower() in ["chest"]:
        print("Ooh, treasure!")
        print("Open it? [1]")
        print("Leave it? [2]")
        choice = input("> ")

        if(choice) == "1":
            print("Lets see whats in here, you say while grinning")
            time.sleep(1)
            print("The chest creaks open, not waking the guard, that's one heavy sleeper.")
            print("You Find: 1x Diamond, 3x Bars of Gold, 2x Bars of Silver, 1x Shiny Sword")
            
            print("What do you want to do?")
            print("Take Items [1]")
            print("Leave Items [2]")

            treasure_choice = input("> ")
            if treasure_choice == "1":
                print("You take the metals and sword from the chest.")
                print(f"You: A new, exceedingly shiny sword! (drops your old, crappy sword in the chest)")
                
                print("You close the chest, leaving your old crappy sword for the next wonderer, now time to get past this sleeping guard.")
            elif treasure_choice == "2":
                print("It'll still be here after I get past this sleeping guard.. I hope at least.")
        elif choice == "2":
            print("Treasure? pfft. Let's get out of here.")
    elif action.lower() in ["guard"]:
        print("Heh, let's have fun with this guard.")
    else:
        print("That's not an option, silly. Let's poke the guard cos it'll be fun!")
    guard()

def right():
    print("You go through the right door and encounter a BIG RED SCARY DRAGON!")
    print("It stares at you through one narrowed eye.")
    print("What do you do? [Flee, Stay]")
    
    next_move = input("> ")

    if "flee" in next_move.lower():
        start()
    else:
        death("You were a tasty snack, wonderer.")

def pname():
    name = input("Welcome, wonderer. What's your name? > ")
    return name

def start():
    doors = input("You enter a room and come across two old, wooden doors. Which one do you go through? [Left, Right] > ")

    if doors.lower() in ["l", "left"]:
        left()
    elif doors.lower() in ["r", "right"]:
        right()
    else:
        print("Wrong choice. goodbye, wonderer.")

def main():
    namep = pname()

    start()

    print("\nThe End\n")
    print(f"Thanks for playing, {namep.upper()}")

if __name__ == '__main__':
    main()
