import time
import os

clear = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

def death(reason):
    print("{} | GG".format(reason))
    exit(0)

def main():
    name = input("What is your name, Agent? [Default: Anton (MALE), Antonia (FEMALE), Alex (NON BINARY / GENDER FLUID)] > ")
    if name == "":
        name = "Anton"
    age = input(f"\nHello, {name}. How old are you? [Default: 34] > ")
    if age == "" or age != int:
        age = 34
    gender = input(f"\nAnd one last thing. What is your gender identity? [Default: MALE] [Choices: MALE, FEMALE, NB, GF] > ")
    if gender == "" or gender.lower() not in ["male", "female", "nb", "nonbinary", "non binary", "gf", "genderfluid", "gender fluit"]:
        gender = "MALE"
    elif gender.lower() == "female":
        name = "Antonia"
    elif gender.lower() in ["nb", "nonbinary", "non binary", "gender fluid", "gf", "genderfluid"]:
        name = "Alex"
    clear()
    print("PLAYER INFORMATION")
    print("Is this correct?\n")
    print(f"Name: {name}\nAge: {age}\nGender Identity: {gender}\n")
    info = input("[Y/N] > ")

    if info.lower() in ["y", "yes"]:
        start()
    elif info.lower() in ["n", "no"]:
        clear()
        main()
    else:
        return
clear()

def camp():
    clear()
    print("You arrive at the Base Camp. Do you want to:")
    print("[1] Get Information\n[2] Talk to the Sargeant \n[3] Leave")
    choice = input("> ")

    if choice == "1":
        clear()
        print("You: Agent, could I have all information on the kidnapping?")
        time.sleep(2)
        print("Agent Carlson: You already have all the information.")
        time.sleep(2.5)
        input("\n[ENTER to continue]")
        camp()
    elif choice == "2":
        clear()
        print("You: Sarge, Do you have any information on the stronghold?")
        time.sleep(2)
        print("Sargeant: It is said the stronghold of the kindapper is located in the Jungle, South West from here.")
        time.sleep(2.5)
        input("\n[ENTER to continue]")
        camp()
    elif choice == "3":
        clear()
        time.sleep(0.5)
        print("Travelling to the Village.")
        time.sleep(1)
        clear()
        print("Travelling to the Village..")
        time.sleep(1)
        clear()
        print("Travelling to the Village...")
        time.sleep(1)
        village()
    elif choice not in ["1", "2", "3"]:
        clear()
        print("Incorrect Selection")
        print("\nChoices:\n[1] Get Information\n[2] Talk to the Sargeant\n[3] Leave")
        time.sleep(2)
        clear()
        time.sleep(0.5)
        camp()

def village():
    clear()
    print("You arrive in the Village, you're surrounded by people. What do you do?")
    print("\n[1] Talk to the kidnappee's parents\n[2] Talk to the locals\n[3] Go to the police station\n[4] Exit the village\n[5] Go back to base")
    choice = input("> ")

    if choice == "1":
        clear()
        print("You: Hello. Are you Mr and Mrs. Garden?")
        time.sleep(2.5)
        print("Mrs. Garden: Yes, we are.")
        time.sleep(2.5)
        print("You: I am investigating the kidnapping of your 13-year-old daughter. Do you have any information about the kidnapping?")
        time.sleep(2.5)
        print("Mr. Garden: Leslie was taken last week at around 12:50 P.M.")
        time.sleep(2.5)
        print("You: Okay, is there anything else that could help with the investigation?")
        time.sleep(2.5)
        print("Mr & Mrs. Garden: I'm afraid not. Please keep us updated, though.")
        time.sleep(2.5)
        input("\n[ENTER to continue]")
        village()
    elif choice == "2":
        clear()
        print("You: Excuse me everyone (you say loudly)")
        time.sleep(1.5)
        print("You: Does anyone have any information on the missing 13-year-old Leslie Garden?")
        time.sleep(2.5)
        print("(No one answers)")
        time.sleep(2.5)
        input("\n[ENTER to continue]")
        village()
    elif choice == "3":
        clear()
        print("You head to the police station, asking for the Cheif Officer.")
        time.sleep(1.5)
        print("\nYou: Excuse me, chief. I need some information on a kidnapping.")
        time.sleep(2.5)
        print("\nPolice Chief: I'm sorry, we're not allowed to disclose any information to locals.")
        time.sleep(2.5)
        input("\n[ENTER to continue]")
        village()
    elif choice == "4":
        clear()
        time.sleep(0.5)
        print("Travelling to the Hills.")
        time.sleep(1)
        clear()
        print("Travelling to the Hills..")
        time.sleep(1)
        clear()
        print("Travelling to the Hills...")
        time.sleep(1)
        hills()
    elif choice == "5":
        clear()
        time.sleep(0.5)
        print("Travelling to Camp.")
        time.sleep(1)
        clear()
        print("Travelling to Camp..")
        time.sleep(1)
        clear()
        print("Travelling to Camp...")
        time.sleep(1)
        camp()
    elif choice not in ["1", "2", "3", "4", "5"]:
        clear()
        print("Incorrect Selection")
        print("Choices:\n[1] Talk to the kidnappee's parents\n[2] Talk to the locals\n[3] Go to the police station\n[4] Exit the village\n[5] Go back to base")
        time.sleep(2)
        clear()
        time.sleep(0.5)
        village()

def hills():
    clear()
    print("You follow the path out of the village, and into the hills. Where do you go next?")
    print("\n[1] Beach\n[2] Jungle\n[3] Village")
    choice = input("> ")

    if choice == "1":
        clear()
        time.sleep(0.5)
        print("Travelling to the Beach.")
        time.sleep(1)
        clear()
        print("Travelling to the Beach..")
        time.sleep(1)
        clear()
        print("Travelling to the Beach...")
        time.sleep(1)
        beach()
    elif choice == "2":
        clear()
        time.sleep(0.5)
        print("Travelling to the Jungle.")
        time.sleep(1)
        clear()
        print("Travelling to the Jungle..")
        time.sleep(1)
        clear()
        print("Travelling to the Jungle...")
        time.sleep(1)
        jungle()
    elif choice == "3":
        clear()
        time.sleep(0.5)
        print("Travelling to the Village.")
        time.sleep(1)
        clear()
        print("Travelling to the Village..")
        time.sleep(1)
        clear()
        print("Travelling to the Village...")
        time.sleep(1)
        village()

def beach():
    clear()
    print("You arrive at the beach. What do you do?")
    print("\n[1] Go back")
    choice = input("> ")

    if choice == "1":
        clear()
        time.sleep(0.5)
        print("Travelling to Hills.")
        time.sleep(1)
        clear()
        print("Travelling to Hills..")
        time.sleep(1)
        clear()
        print("Travelling to Hills...")
        time.sleep(1)
        hills()
    elif choice not in ["1"]:
        clear()
        print("Incorrect Selection")
        print("Choices:\n[1] Go back")
        time.sleep(2)
        clear()
        time.sleep(0.5)
        beach()

def jungle():
    clear()
    print("You arrive at the jungle and immediately see two men sleeping in front of a door with automatic rifles next to each of them. What do you do?")
    print("\n[1] Flee\n[2] Sneak past them")
    choice = input("> ")

    if choice == "1":
        clear()
        time.sleep(0.5)
        print("Travelling to Hills.")
        time.sleep(1)
        clear()
        print("Travelling to Hills..")
        time.sleep(1)
        clear()
        print("Travelling to Hills...")
        time.sleep(1)
        hills()
    elif choice == "2":
        stronghold()
    elif choice not in ["1", "2"]:
        clear()
        print("Incorrect Selection")
        print("Choices:\n[1] Flee\n[2] Sneak past them")
        time.sleep(2)
        clear()
        time.sleep(0.5)
        jungle()

def stronghold():
    clear()
    print("You sneak past the guards and are now in the stronghold. To your left is 13-year-old Leslie Garden, and to your right is a guard. What do you do?")
    print("\n[1] Get Leslie and sneak out\n[2] Flee")
    choice = input("> ")

    if choice == "1":
        clear()
        escaped()
    elif choice == "2":
        clear()
        death("You ran out of the stronghold and were stopped by the two armed guards, one shooting you in the head and the other shooting you in the heart.")
    elif choice not in ["1", "2"]:
        clear()
        print("Incorrect Selection")
        print("Choices:\n[1] Flee\n[2] Sneak past them")
        time.sleep(2)
        clear()
        time.sleep(0.5)
        stronghold()

def escaped():
    clear()
    print("GG! You escaped with Lesie Garden, reunited her with her family and went back to base, where you were promoted to Sargeant.")
    print("\nThanks for playing!")
    time.sleep(3)
    input("[ENTER] to continue")
    return

def start():
    clear()
    print("Where would you like to start?\n")
    print("[1] Village\n[2] Base Camp\n[3] Jungle")
    choice = input("> ")
    if choice == "1":
        village()
    elif choice == "2":
        camp()
    elif choice == "3":
        jungle()
    elif choice not in ["1", "2", "3"]:
        clear()
        print("Incorrect Selection")
        print("\nChoices:\n[1] Village\n[2] Base Camp\n[3] Jungle")
        time.sleep(2)
        clear()
        time.sleep(0.5)
        start()

print("You have a mission. You must rescue 13-year-old Leslie Garden, a kidnapped young girl. It is said the kidnapper is keeping her in their stronghold. You will have to break into said stronghold, rescue the kidnapped, break out, and escape back to safety; this requires careful and clever planning, as well as a large dose of luck. Good luck, Agent.")
time.sleep(3)
input("\n[ENTER to continue]")

clear()
main()

if __name__ == '__main__':
    main()