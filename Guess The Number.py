import random
from Save_record import Save_record
from datetime import datetime

class Guessthenumber:
    def __init__(self, lower, upper, Player_name, game_name="Guess the Number , Date_time : "+ datetime.now().strftime('%Y-%m-%d %H:%M:%S')):
        # Initialize game parameters
        self.game_name = game_name
        self.lower = int(lower)  # Convert lower bound to integer
        self.upper = int(upper)  # Convert upper bound to integer
        self.guess_number = random.randint(self.lower, self.upper)  # Random number to guess
        self.guesses = 0  # Count of guesses made
        self.Player_name = Player_name  # Name of the player
        self.save_record = Save_record()  # Instance of Save_record class for saving game records

    def make_guess(self, guess):
        # Increment guess count
        self.guesses += 1
        guess = int(guess)  # Convert guess to integer
        if guess > self.guess_number:
            return "Lower"  # Provide hint if guess is higher than the target number
        elif guess < self.guess_number:
            return "Higher"  # Provide hint if guess is lower than the target number
        else:
            return "Correct"  # Return "Correct" if the guess matches the target number

    def reset_game(self):
        # Reset the game with a new random number and reset guess count
        self.guess_number = random.randint(self.lower, self.upper)
        self.guesses = 0

    def play(self):
        # Start the game and prompt the player for guesses
        print(f"Hey {self.Player_name}! Guess the number between {self.lower} and {self.upper}")
        while True:
            try:
                guess = int(input("Enter your guess: "))  # Get the player's guess
                result = self.make_guess(guess)  # Check the guess and get the result
                print(result)  # Print the result
                if result == "Correct":
                    # Print final result and save the record if the guess is correct
                    self.final_result = f"Congratulations {self.Player_name}! You guessed the number in {self.guesses} tries."
                    print(self.final_result)
                    self.save_record.save_record(self.game_name, self.Player_name, f"{self.Player_name} Win! in {self.guesses} tries.")
                    break
            except ValueError:
                # Handle invalid input (non-integer values)
                print("Please enter a valid number.")

if __name__ == "__main__":
    while True:
        try:
            print("Wel-Come")
            print("??????????????????Guessing Game??????????????????")
            player_name = input("Write your name: ")
            if not player_name.isalpha():  # Check if player_name contains only alphabetic characters
                raise ValueError("Player name must contain only alphabetic characters.")
            
            lower = int(input("Write the lower number: "))  # Get the lower bound for the guessing range
            upper = int(input("Write the upper number: "))  # Get the upper bound for the guessing range
            
            game = Guessthenumber(lower, upper, player_name)  # Create a new game instance
            game.play()  # Start the game
            break
        except ValueError as e:
            # Handle invalid input for name or number bounds
            print(f"Invalid input: {e}")
