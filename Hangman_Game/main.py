import hangman

word = hangman.get_word()
word_length = hangman.get_word_length(word)
hangman.welcome(word_length)
word_display = hangman.get_word_display(word)
hangman.display_word(word_display)
max_attempts = hangman.get_word_length(word) + 2
attempts = 0

while '_' in word_display and attempts < max_attempts:
    letter = input('Enter a letter: ')
    if letter in word:
        hangman.update_word_display(word, word_display, letter)
        hangman.display_word(word_display)
    else:
        attempts += 1
        print(f"Incorrect guess! {max_attempts - attempts} attempts left.")

   
if '_' not in word_display:
    print('You win!')
else:
    print('You lose! The word was:', word)
