import random
import string
from random import randrange


def random_mail(char_num):
    return ''.join(random.choice(string.ascii_letters) for _ in range(char_num)) + "@gmail.com"


def random_word(char_num):
    return ''.join(random.choice(string.ascii_letters) for _ in range(char_num))


def random_number():
    return randrange(100)