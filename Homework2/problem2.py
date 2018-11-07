import random

num = random.randint(1,100)
guess = input("Guess the number... ")

guesses = 0
while (guess) != num and (guess) != "exit":

    if int(guess) > num:
        guess = input("You guessed too high.")
        guesses += 1
 
    elif int(guess) < num:
        guess = input("You guessed too low.")
        guesses += 1
if (guess) == "exit":
        exit (0)    

print ("Well done! ","You guessed with " + str(guesses) + " guesses")
