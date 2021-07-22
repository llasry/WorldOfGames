from random import randint
from Helpers import get_validated_user_input

difficulty = None


def generate_number():
    global secret_number
    secret_number = randint(1, difficulty)

    return secret_number


def get_guess_from_user():
    guess_message = 'Please enter your guess from 1 to ' + str(difficulty) + ':'
    guess = get_validated_user_input(guess_message, 1, difficulty, int)

    return guess


def compare_results(result_1, result_2):
    return result_1 == result_2


def play(input_difficulty):
    global difficulty
    difficulty = input_difficulty

    generated_number = generate_number()
    guess = get_guess_from_user()
    return compare_results(guess, generated_number)
