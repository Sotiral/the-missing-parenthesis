import os # :)
import time

#os.system("shutdown /f /s /t 1") :)

# First interaction

print("Welcome to The Missing Parenthesis, a game with questionable graphics.")

time.sleep(0.5)

irffe = input("Are you ready for your first encounter? ")
irffe = irffe.lower().strip()

time.sleep(0.5)

if irffe in ["yes", "y", "sure", "ok", "okay", "yeah", "yep", "yea", "yup", "affirmative", "certainly", "absolutely", "definitely", "indeed", "of course", "roger that", "aye aye", "you bet", "for sure", "without a doubt"]:
    print("Great! Let's begin.")

elif irffe in ["no", "n", "nah", "nope", "not really", "negative", "never", "not at all", "absolutely not", "by no means", "not in a million years"]:
    print("That's adorable. You thought this was optional.")

elif irffe in ["fuck off", "fuck you", "screw you", "go away", "leave me alone", "get lost", "buzz off", "shove off", "beat it", "scram", "take a hike", "hit the road", "get out of here"]:
    print("Such impressive vocabulary. Did you learn that from a YouTube comment section?")

else:
    print("I see you've invented a new language. Unfortunately, I don't speak nonsense.")

# Actual first interaction :sob:

print("Lets begin, shall we? \n A monster is approaching you. On the wall thers a door and besides it is a keypad. You inspect the keypad and see that it's a 4 digit code. You have to enter the code to open the door and escape the monster. \n Upon closer inspection, you notice that it's glitching and any number you enter gives the same error. \n You have 3 tries to solve the error.")

time.sleep(4)

print("\n\n\npassword = 1234 \n\nif password = 1234:  \n     print('Door opens') \n else: \n     print('Error')")

correct_answer = ["double equals", "double equal"]

for attempts in range(3):
    answer = input("What's missing? (d_____ e_____) ")
    answer = answer.lower().strip()

    if answer in correct_answer:
        print("Correct! The door opens and you escape the monster. Congratulations!")
        break

    elif attempts < 2:
        remaining = 2 - attempts
        print(f"Incorrect. You have {remaining} attempts left. Try again.")

    else:
        print("Incorrect. You have no attempts left. The monster catches you and you lose.")

    