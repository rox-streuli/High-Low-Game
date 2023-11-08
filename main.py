import random
from game_art import logo

# Constants
EASY = 10
MEDIUM = 7
HARD = 5

def check_guess(guess, number):
    """Compare user guess and number to guess."""
    if guess < number:
        return "Too low, guess higher.\n"
    elif guess > number:
        return "Too high, guess lower.\n"
    else:
        return


def choose_difficulty():
    """Set dificulty level."""
    chossing = input("Choose difficulty:"
                     "\n'1' for EASY "
                     "\n'2' for MEDIUM "
                     "\n'3' for HARD"
                     "\n--> ").lower()
    if chossing  == '1':
        return EASY
    elif chossing == '2':
        return MEDIUM
    elif chossing == '3':
        return HARD
    else:
        choose_difficulty()


def guess_number() -> int:
    """Ask the player to guess the number. Only intigers allowed."""
    try:
        guessing = int(input("Guess a number: "))
    except:
        print("Try again. Please only integers.")
        guess_number()
    else:
        return guessing


def play_again() -> str:
    """Ask user to play again or close game."""
    answer = 'q'
    while answer not in 'yn':
        answer = input("Type 'y' to play again "
                   "or 'n' to quit. ").lower()
    return answer


play = True

while play:
    print(logo)
    attempts = 0
    print("\nWelcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")
    number_to_guess = random.randint(1, 100)
    attempts = choose_difficulty()

    while attempts > 0:
        print(f"You have {attempts} remaining to guess the number.")
        attempts -= 1
        user_guess = guess_number()
        did_i_win = check_guess(user_guess, number_to_guess)
        if did_i_win == None:
            print("*" * 30)
            print(f"Well done! You won! It was {number_to_guess}")
            print("*" * 30, "\n")
            break
        else:
            print(did_i_win)
    else:
        print(f"You run out of attempts. Nice try. "
              f"The number was {number_to_guess}.\n")
    user_answer = play_again()
    play = True if user_answer == 'y' else False

print("Closing game.")
