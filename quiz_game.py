from calendar import monthcalendar


print("Welcome to Learning About Essence")
username = input("What is your name? ")
print("Hello " + username.upper() + ", want to play a game?")
playing = input()


if playing.lower() == "yes":
    print("Yay in a few short questions you will know more about me :)")
else:
    print("We shall play either way")
score = 0
#print("Okay let's play!")

q_1 = input("Is my favorite color blue? ").lower()

while (q_1 != "no" or "yes"):
    if q_1 == "no":
        print("You're right! My favorite color is purple :) ")
        score += 1
    elif q_1 == "yes":
        print("Not quite! My favorite color is purple")
    else:
        print("Invalid response. Reply yes or no!")
        q_1 = input("Is my favorite color blue? ").lower()
        continue
    break
q_2 = input("Is my favorite food steak? ").lower()

while q_2 != "no" or "yes":
    if q_2 == "no":
        print("Not quite. I love steak!")

    elif q_2 == "yes":
        print("That's correct!")
        score += 1
    else:
        print("Invalid response. Reply yes or no")
        q_2 = input("Is my favorite food steak? ").lower()
        continue
    break

q_3 = input("Do I love coding? ").lower()

while q_3 != "no" or "yes":
    if q_3 == "no":
        print("Not quite. I love coding! ")
    elif q_3 == "yes":
        print("Absolutely!")
        score += 1
    else:
        print("Invalid response. Reply yes or no!")
        q_3 = input("Do I love coding? ").lower()
        continue
    break

print("You got", score, "questions correct.")
