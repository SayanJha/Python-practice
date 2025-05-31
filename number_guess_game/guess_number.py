import random

def guess(x):
    random_number = random.randint(1, x)
    print("Guess a number or press \"q\" anywhere to quit: ")
    while True:
        try:
            user_guess = (input(f"Guess a number between 1 and {x}: "))
            if user_guess.strip().lower() == "q":
                print("Exiting...")
                break

            user_guess = int(user_guess)
            if not (1 <= user_guess <= x):
                print(f"Enter a number between 1 and {x}!")
                continue
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue

        if user_guess > random_number:
            print("Too high!")
        elif user_guess < random_number:
            print("Too low!")
        else:
            print(f"You guessed the correct number: {random_number} :)")
            break

if __name__ == "__main__":
    guess(10)