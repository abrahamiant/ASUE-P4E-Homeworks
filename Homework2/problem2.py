import random
  
generated_number = random.randint(1,100)
num_of_guesses =  0
guessed_number = 0

while int(guessed_number ) != generated_number:
    guessed_number = input("Guess the  number...")

    if guessed_number == exit :
        break

    num_of_guesses += 1

    if int(guessed_number ) > generated_number:
      print("You guessed too high.")

    elif int(guessed_number) < generated_number:
      print ("You guessed too low.")
else:
    print("Well done!")
    print("You guessed it in " +  str(num_of_guesses) +  " steps")


