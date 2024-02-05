import secrets
import string

def Password_gen(length: int) -> str:
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation

    combination = letters + digits + special_chars

    psswd = ''.join(secrets.choice(combination) for _ in range(length))

    return psswd