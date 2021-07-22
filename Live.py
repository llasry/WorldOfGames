import GuessGame
import MemoryGame
import CurrencyRouletteGame
from Helpers import get_validated_user_input


def welcome(name):
    return 'Hello ' + name + ' and welcome to the World of Games (WoG).\n' + 'Here you can find many cool games to play.'


def print_result(result):
    if result:
        print("You Won!!!")
    else:
        print("You Lost :(  No worries, try again...")


def load_game():
    game_message = 'Please choose a game to play:\n' \
                   '1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back\n' \
                   '2. Guess Game - guess a number and see if you chose like the computer\n' \
                   '3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n'

    difficulty_message = 'Please choose game difficulty from 1 to 5:'

    game = get_validated_user_input(game_message, 1, 3, str)

    difficulty = get_validated_user_input(difficulty_message, 1, 5, int)

    if game == '1':
        print_result(MemoryGame.play(difficulty))
    elif game == '2':
        print_result(GuessGame.play(difficulty))
    elif game == '3':
        print_result(CurrencyRouletteGame.play(difficulty))
