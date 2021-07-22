import random
import time
import sys


def generate_sequence(length_of_sequence):
    sequence = random.sample(range(1, 101), length_of_sequence)

    return sequence


def get_list_from_user(length_of_list):
    list_message = '\rPlease guess the ' + str(length_of_list) + ' numbers between 1 to 101 (e.g. 12 67 23 56...):'

    input_valid = False
    while not input_valid:
        try:
            list_from_user = list(map(int, input(list_message).strip().split()))
            if len(list_from_user) == length_of_list:
                if all(map(lambda list_element: 1 <= list_element <= 101, list_from_user)):
                    input_valid = True
                else:
                    print("Invalid input. Numbers not between 1 and 101. Please try again.")
            else:
                print("Invalid input. Number of numbers provided is not " + str(length_of_list) + ". Please try again.")
        except ValueError:
            print("Invalid input. Bad values entered. Please try again.")

    return list_from_user


def is_list_equal(list_1, list_2):
    return list_1 == list_2


def play(difficulty):
    generated_sequence = generate_sequence(difficulty)
    print(generated_sequence, end="")
    time.sleep(0.7)
    sys.stdout.flush()

    user_sequence = get_list_from_user(difficulty)

    return is_list_equal(generated_sequence, user_sequence)

