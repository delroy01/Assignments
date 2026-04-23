import random

def start_game():
    secret_number = random.randint(1, 100)
    attempts = 0
    guessed_correctly = False
    
    print("--- Simple Number Guessing Game ---")
    print("I'm thinking of a number between 1 and 100.")
    
    # Loop until the number is guessed
    while not guessed_correctly:
        try:
            user_guess = int(input("Enter your guess: "))
            attempts += 1
            
            if user_guess < secret_number:
                print("Too low! Try again.")
            elif user_guess > secret_number:
                print("Too high! Try again.")
            else:
                guessed_correctly = True
                print(f"\n Congratulations! You guessed it.")
                print(f"It took you {attempts} attempts.")
                
        except ValueError:
            print("Please enter a valid whole number.")
            
if __name__ == "__main__":
    start_game()