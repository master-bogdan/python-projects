import random
import os
from hangman_words import word_list
from hangman_art import stages, logo

end_of_game = False
chosen_word = random.choice(word_list)
chosen_word_len = len(chosen_word)
lives = 6

display = ['_'] * chosen_word_len

print(logo)

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    os.system('clear')

    if guess in display:
        print(f'You already guessed letter ${guess}')

    for position in range(chosen_word_len):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f'{guess} is not in the word. You loose a life')
        lives -= 1

        if lives == 0:
            end_of_game = True
            print('You loose')

    print(display)

    if '_' not in display:
        end_of_game = True
        print('You win')

    print(stages[lives])
