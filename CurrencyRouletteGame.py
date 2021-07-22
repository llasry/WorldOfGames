import sys
import requests
from random import randint
from Helpers import get_validated_user_input


def get_money_interval(number, difficulty):
    exchange_rates_json = requests.get('https://api.coinbase.com/v2/exchange-rates').json()
    usd_to_ils_exchange_rate = float(exchange_rates_json['data']['rates']['ILS'])
    total_value_of_money = number * usd_to_ils_exchange_rate

    return total_value_of_money - (5 - difficulty), total_value_of_money + (5 - difficulty)


def get_guess_from_user(amount):
    guess_message = 'Amount in USD is ' + str(amount) + '$. What\'s your estimation for the amount in ILS?'
    guess = get_validated_user_input(guess_message, 0, sys.maxsize, float)

    return guess


def play(difficulty):
    usd_amount = randint(1, 100)
    user_ils_amount_guess = get_guess_from_user(usd_amount)
    accepted_interval = get_money_interval(usd_amount, difficulty)

    return  accepted_interval[0] <= user_ils_amount_guess <= accepted_interval[1]
