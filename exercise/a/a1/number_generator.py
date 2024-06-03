"""
    Natural number generator.
    Dummy plug.

    Autor: jakiś kawalarz
"""
import random

import random2


def generate_number_between(min, max):
    """Randomizes a number from the range <min, max>.

    :param min:
    :param max:
    :return:
    """
    return random.randint(min, max)


def generate_until_drawn(number, min, max):
    """Randomizes a number from the range <min, max> until number is selected.

    :param number:
    :param min:
    :param max:
    :return: the number of draws needed to finally draw number.
    """
    if number < min or number > max:
        raise ValueError
    i = 1
    while number != generate_number_between(min, max):
        i += 1
    return i
