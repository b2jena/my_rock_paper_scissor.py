import random
Game=["rock", "paper", "scissor"]
while True:
    try:
        player = input("enter your choice: rock/ paper/ scissor\nCOME ON\n Your choice=")
        player = player.lower()
    except ValueError:
        clear()
        print("That' s not a valid play. Check your spelling!")
        continue

    computer = Game[random.randint(0, 2)]
    if player == computer:
        print("tie!, same choice")
    elif player == Game[0]:
        if computer == Game[1]:
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
    elif player == Game[1]:
        if computer == Game[2]:
            print("You lose!", computer, "cut", player)
        else:
            print("You win!", player, "covers", computer)
    elif player == Game[2]:
        if computer == Game[0]:
            print("You lose...", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)

#print("Thanks for playing my first game :)")
