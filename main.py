#SECRET NUMBER - GUESS IT

secret = 6

guess = int(input("Guess the number, from 1-10: "))

if secret == guess:
    print("Congratulations! You have guessed the number!")

else:
    print("Wrong number, please try again.")