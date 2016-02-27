from hero import Hero

def main():
    char = Hero()

    print("Welcome to the adventure!")
    char.title = raw_input("Choose your name, hero: ")
    print("Let us begin...\n")
    print("You start by waking up in a dark cold forest...\n\n")
    print("What would you like to do first?")
    print("1. Anal?")
    print("2. Anal?")
    print("3. Anal?")
    choice = int(raw_input("Make your choice: "))
    #equal = (choice == 1)
    #print"choice = %d, %d == 1, %r" % (choice, choice, equal)
    while (choice != 1 and choice != 2 and choice != 3):
        #print("That is not a valid input. Please choose again.")
        #choice = raw_input("Make your choice.")
        choice = int(raw_input("That is not a valid input. Please choose again."))

main()
