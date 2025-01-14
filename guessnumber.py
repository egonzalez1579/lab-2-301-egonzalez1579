print("Welcome to the gae of guessing numbers")

secret_number = 1
chances = 5



while chances <= chances:
    userGuessNumber = int(input("Guess a random number between 1 and 100: "))
    if userGuessNumber == secret_number:
        print("Congratulation You guessed right!")
        break
    else:
        print("Sorry, you didn't guess right.")

chances = chances - 1