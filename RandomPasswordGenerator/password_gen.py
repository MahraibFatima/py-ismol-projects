import random
import string

def Password_gen(length: int) -> str:
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation

    combination = letters + digits + special_chars

    return "".join(random.sample(combination, length))
