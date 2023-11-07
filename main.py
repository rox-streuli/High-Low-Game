import random
from game_art import logo

def check_guess(guess, number):
    if guess < number:
        return "Too low, guess higher.\n"
    elif guess > number:
        return "Too high, guess lower.\n"
    else:
        return


def choose_difficulty():
    chossing = input("Choose a difficulty.Type 'e' for easy or 'h' "
                     "for hard. ").lower()
    if chossing in "eh":
        return chossing
    else:
        choose_difficulty()


def guess_number():
    try:
        guessing = int(input("Guess a number: "))
    except:
        print("Try again. Please only integers.")
        guess_number()
    else:
        return guessing


def play_again():
    answer = 'q'
    while answer not in 'yn':
        answer = input("Type 'y' to play agay "
                   "or 'n' to quit. ").lower()
    return answer


play = True

while play:
    print(logo)
    attempts = 0
    number_to_guess = random.randint(1, 100)
    print("\nWelcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")
    difficulty = choose_difficulty()

    if difficulty == "e":
        attempts = 10
    else:
        attempts = 5

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
