print("Made by Shashi")
loose=("The computer wins")
win=("You win")
lives=5
score=0
drew=0
computer_lives=7
while True :
    print("To begin fill in the below information")
    username = input("Please enter your username")
    password = input("Please enter your password")
    searchfile = open("accounts.csv","r")
    for line in searchfile:
        if username and password in line:
            print("Acess Granted")
            print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
            print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
            print("    ___                  ______________     ______________     _______________     ____      ___     ")
            print("  ¦   ¦                ¦              ¦   ¦              ¦   ¦               ¦   ¦    ¦    /   /     ")
            print(" /------------------     ¦     ___      ¦   ¦  __________  ¦   ¦  _____________¦   ¦    ¦   /   /    ")
            print("/            \     ¦     ¦    ¦   ¦     ¦   ¦ ¦          ¦ ¦   ¦ ¦                 ¦    ¦  /   /     ")
            print("¦       ------------     ¦    ¦___¦   __¦   ¦ ¦          ¦ ¦   ¦ ¦                 ¦    ¦_/   /      ")
            print("¦       ------------     ¦           \      ¦ ¦          ¦ ¦   ¦ ¦                 ¦         /       ")
            print("¦            \     ¦     ¦    ¦\      \     ¦ ¦          ¦ ¦   ¦ ¦                 ¦    ¦\   \       ")
            print("¦       ------------     ¦    ¦ \      \    ¦ ¦__________¦ ¦   ¦ ¦_____________    ¦    ¦ \   \      ")
            print("¦       ------------     ¦    ¦  \      \   ¦              ¦   ¦               ¦   ¦    ¦  \   \                   ___  ___  ___  ___")
            print("¦            \     ¦     ¦____¦   \______\  ¦______________¦   ¦_______________¦   ¦____¦   \___\                 ¦   ¦¦   ¦¦   ¦¦   ¦")
            print("¦       ------------                                                                                          ___ ¦   ¦¦   ¦¦   ¦¦   ¦")
            print("\       ------------ ___________     _______________     ___________     ___________     _____________       ¦   ¦¦   ¦¦   ¦¦   ¦¦   ¦")
            print(" \           \     /¦   _____   ¦   ¦     _____     ¦   ¦   _____   ¦   ¦           ¦   ¦             ¦      ¦   ¦¦   ¦¦   ¦¦   ¦¦   ¦")
            print(" \---------------/ ¦  ¦     ¦  ¦   ¦    ¦_____¦    ¦   ¦  ¦     ¦  ¦   ¦    _______¦   ¦     ___     ¦      ¦   ¦¦   ¦¦   ¦¦   ¦¦   ¦")
            print("                   ¦  ¦_____¦  ¦   ¦     _____     ¦   ¦  ¦_____¦  ¦   ¦   ¦           ¦    ¦   ¦    ¦      ¦   ¦¦   ¦¦   ¦¦   ¦¦   ¦")
            print("                   ¦    _______¦   ¦    ¦     ¦    ¦   ¦    _______¦   ¦   ¦_____      ¦    ¦___¦   _¦      \                       /")
            print("                   ¦   ¦           ¦    ¦     ¦    ¦   ¦   ¦           ¦    _____¦     ¦           \         \                     /")
            print("                   ¦   ¦           ¦    ¦     ¦    ¦   ¦   ¦           ¦   ¦_______    ¦    ¦\      \         \                   /")
            print("                   ¦   ¦           ¦    ¦     ¦    ¦   ¦   ¦           ¦           ¦   ¦    ¦ \      \         \                 /   ")
            print("                   ¦___¦           ¦____¦     ¦____¦   ¦___¦           ¦___________¦   ¦____¦  \______\         \_______________/                                /     /")
            print("                                                                                                                                                                /     /")
            print(" ______________     _______________     ____     ______________     ______________     ______________     _____________     ______________                    /     /")
            print("¦   ___________¦   ¦               ¦   ¦    ¦   ¦   ___________¦   ¦   ___________¦   ¦              ¦   ¦             ¦   ¦   ___________¦    ________    /     /")
            print("¦  ¦               ¦  _____________¦   ¦    ¦   ¦  ¦               ¦  ¦               ¦  __________  ¦   ¦     ___     ¦   ¦  ¦               /          /     /")
            print("¦  ¦___________    ¦ ¦                 ¦    ¦   ¦  ¦___________    ¦  ¦___________    ¦ ¦          ¦ ¦   ¦    ¦   ¦    ¦   ¦  ¦___________   ¦         /     /")
            print("¦____________  ¦   ¦ ¦                 ¦    ¦   ¦____________  ¦   ¦____________  ¦   ¦ ¦          ¦ ¦   ¦    ¦___¦   _¦   ¦____________  ¦  ¦       /     /")
            print("            ¦ ¦   ¦ ¦                 ¦    ¦                ¦ ¦                ¦ ¦   ¦ ¦          ¦ ¦   ¦           \                  ¦ ¦  ¦               __________________")
            print("            ¦ ¦   ¦ ¦_____________    ¦    ¦                ¦ ¦                ¦ ¦   ¦ ¦__________¦ ¦   ¦    ¦\      \                 ¦ ¦  ¦                                 ¦")
            print(" ____________¦ ¦   ¦               ¦   ¦    ¦    ____________¦ ¦    ____________¦ ¦   ¦              ¦   ¦    ¦ \      \    ____________¦ ¦  ¦               __________________¦")
            print("¦______________¦   ¦_______________¦   ¦____¦   ¦______________¦   ¦______________¦   ¦______________¦   ¦____¦  \______\  ¦______________¦  ¦______________¦")
            print("                                                                                                                                                                                  ")
            print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
            print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
            print("lives Rules ")
            print("You start with",lives,"lives")
            print("If you win you get a extra lives. ")
            print("If you loose you loose a lives. ")
            print("If you draw the lives stay the same")
            print("_________________________________________")
            print("MAKE SURE YOU DON'T USE CAPITALS")
            print("_________________________________________")
            print("To see a list of rules type rules")
            print("_________________________________________")
            print("At any point exit to leaves the game.")
            print("_________________________________________")
            print("The computer has lives aswell")
            print("Can you beat the computer")
            print("Good Luck")
            print("_________________________________________")
            while True:
                rps=input("Rock, Paper, Scissors?")
                rps=rps.title()
                import random
                computer = ("rock","paper", "scissor")
                computer = random.choice(computer)
            #if rock if statements
                if rps == "rock" and computer == "paper":
                    print("The computer choice ",computer)
                    print("")
                    print(loose)
                    print("")
                    lives-=1
                elif rps == "rock" and computer == "scissor" :
                    print("The computer choose",computer)
                    print("")
                    print(win)
                    computer_lives-=1
                    print("")
                    print("")
                    score+=1
            #paper if statements
                elif rps == "paper" and computer == "rocks" :
                    print("The computer choose", computer)
                    print("")
                    print(win)
                    computer_lives-=1
                    print("")
                    print("")
                    score+=1
                elif rps == "paper" and computer == "scissors":
                    print("The computer choose", computer)
                    print("")
                    print(loose)
                    print("")
                    print("")
                    lives-=1
                #scissor if statements
                if rps == "scissors" and computer == "paper":
                    print("The computer choose",computer)
                    print("")
                    print(win)
                    computer_lives-=1
                    print("")
                    print("")
                    score+=1
                elif rps == "scissors" and computer == "rock" :
                    print("The computer choose",computer)
                    print("")
                    print(loose)
                    print("")
                    print("")
                    lives-=1
                #duplicates
                elif rps == "rock" and computer == "rock" :
                    print("The computer choose",computer)
                    print("")
                    print("You drew")
                    print("")
                    print("")
                    drew+=1
                elif rps == "paper" and computer == "paper" :
                    print("The computer choose",computer)
                    print("")
                    print("You drew")
                    print("")
                    print("")
                    drew+=1
                elif rps == "scissors" and computer == "scissors" :
                    print("The computer choose",computer)
                    print("")
                    print("You drew")
                    print("")
                    print("")
                    drew+=1
                #system
                elif rps == "rules":
                    print("**********************************************")
                    print("Rules")
                    print("**********************************************")
                    print("-Rock looses against Paper")
                    print("-Rock beats Scissors")
                    print("-Paper beats Rock")
                    print("-Paper looses against Scissors")
                    print("-Scissors beats Paper")
                    print("-Scissors looses against Rock")
                    print("**********************************************")
                elif rps == "display lives":
                    print(lives)
                elif rps == "display score":
                    print(score)
                elif rps == "display drew":
                    print(drew)
                #lives
                elif lives == 0 or rps == "test":
                    print("Thanks for playing")
                    print("You have run out of lives")
                    print("You got",score,"correct")
                    print("You drew",drew,"times")
                    stop = input("Press enter to exit")
                    import time
                    time.sleep(900)
                elif computer_lives == 0:
                    print("Thanks for playing.")
                    print("The computer lost all it's lives. You win.")
                    print("You got", score, "correct")
                    print("You drew", drew, "times")
                    stop = input("Press enter to exit")
                    import time
                    time.sleep(900)
                #exit
                elif rps == "exit":
                    break
        else:
         print("Your username or password is incorrect.")
         print("_______________________________________")








