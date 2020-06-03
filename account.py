print("_______________________________________")
print("Rock, Paper, Scissors Account Setup")
while True:
    username=input("Pick a Username")
    password=input("Pick your password")
    password_confirm=input("Please confirm your password")

    if password != password_confirm:
        print("Your password don't match. Please try again.")
    if password == password_confirm :
        print("Your account has been setup.")
        text_file = open("accounts.csv","a")
        text_file.write(",")
        text_file.write(username)
        text_file.write(",")
        text_file.write(password)
        text_file.close()
        break