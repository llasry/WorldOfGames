def is_number(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


def validate_number_in_range(number, low, high):
    return is_number(number) and low <= float(number) <= high


def get_validated_user_input(message, lower_bound, upper_bound, cast_func):
    user_input = input(message)
    while not validate_number_in_range(user_input, lower_bound, upper_bound):
        user_input = input('invalid input !!!\n' + message)

    return cast_func(user_input)
