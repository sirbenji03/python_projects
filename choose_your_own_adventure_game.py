name = input("Type your name here: ")
print("welcome", name, "to this adventure")

answer = input(
    "you are on a dirt road, it has come to an end you can go to the left or right. Which way would you like to go? ").lower()

if answer == "left":
    answer = input(
        "You come to a river. Do you want to go around it or swim. type walk to walk around it or swim to swim across it: ")
    if answer == "swim":
        print("You swam dumbass and was eaten by an alligator.")
    elif answer == "walk":
        print("You walked for 100 miles and ran out of oxygen and lost the game.")
    else:
        print("not a valid answer. Please try. ")


elif answer == "right":
    answer = input(
        "you came to an old bridge which looks woobly. do you wanna cross or head back (cross/back)? ")

    if answer == "back":
        print("You go back and lose.")
    elif answer == "cross":
        answer = input(
            "You cross the bridge and met a stranger.Do you talk to them (yes/no)? ")
        if answer == "yes":
            print("You talk to the stranger and the gave you diamond. You win!")
        elif answer == "no":
            print("You ignored the stranger and hence you lose")
    else:
        print("you lost, not a valid option")

else:
    print("you lost, not a valid option")

print("Thank you for trying", name)
