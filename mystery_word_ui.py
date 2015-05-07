import random

from mystery_word import *


guesses = []

def main(starting_word_list):
    word_list = choose_difficulty(starting_word_list)
    print(word_list)
    word = random_word(word_list)
    print('The mystery word has {} letters. Good luck!'.format(len(word)))
    make_guess()

def choose_difficulty(starting_word_list):
    """Asks user for difficulty level and passes appropriate word list function"""
    levels = {'E': easy_words, 'N': medium_words, 'H': hard_words}
    selection = ''
    while selection not in levels:
        selection = input('Please choose [E]asy, [N]ormal, or [H]ard mode: ').upper()
    level = levels[selection]
    return level(starting_word_list)

def make_guess():
    guess = ''
    while (not guess.isalpha()) and len(guess) != 1 :
        guess = input('Please guess a letter: ').lower()

    guesses.append(guess)

def get_starting_word_list(filename='/usr/share/dict/words'):
    """Takes filename and filters into list of lowercase words"""
    pass

if __name__ == '__main__':
    word_list = ["bird", "calf", "river", "stream", "kneecap",  "cookbook",
                 "language", "sneaker", "algorithm", "integration", "brain"]

    main(word_list)
