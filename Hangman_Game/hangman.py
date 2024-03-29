import random

word_list = word_list = ['apple', 'banana', 'cherry', 'date', 'elderberry', 
                        'fig', 'grape', 'honeydew', 'kiwi', 'lemon', 'mango', 'nectarine', 
                        'orange', 'papaya', 'quince', 'raspberry', 'strawberry', 'tangerine', 
                        'watermelon', 'blueberry', 'blackberry', 'cranberry', 'boysenberry', 
                        'pineapple', 'coconut', 'pear', 'plum', 'apricot', 'guava']


def welcome(word_length):
    print('Welcome to Hangman!')
    print(f'The word has {word_length} letters.')
    print('Try to guess the word one letter at a time.')

def get_word():
    return random.choice(word_list)

def get_word_length(word):
    return len(word)

def get_word_display(word):
    return ['_' for _ in word]

def display_word(word_display):
    print(' '.join(word_display))

def update_word_display(word, word_display, letter):
    for i in range(len(word)):
        if word[i] == letter:
            word_display[i] = letter
