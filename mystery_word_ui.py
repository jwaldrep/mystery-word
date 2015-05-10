import random

from mystery_word import *


guesses = []

def main(starting_word_list):
    word_list = choose_difficulty(starting_word_list)
    print(word_list)
    word = random_word(word_list)
    print('The mystery word has {} letters. Good luck!'.format(len(word)))
    print('The mystery word is {}'.format(word))
    print(make_guess(word, word_list))

def choose_difficulty(starting_word_list):
    """Asks user for difficulty level and passes appropriate word list function"""
    levels = {'E': easy_words, 'N': medium_words, 'H': hard_words}
    selection = ''
    while selection not in levels:
        selection = input('Please choose [E]asy, [N]ormal, or [H]ard mode: ').upper()
    level = levels[selection]
    return level(starting_word_list)

def query_letter(): #make_guess(word, word_list):
    guess = ''
    while (not guess.isalpha()) or len(guess) != 1 :
        guess = input('Please guess a letter: ').lower()

    is_good_guess = check_letter(guess, word, word_list)
    if is_good_guess == None:
        print('You already guessed that!')
        guess = input('Please guess a letter: ').lower()


    #guesses.append(guess)
    return is_good_guess

def get_starting_word_list(filename='/usr/share/dict/words'):
    """Takes filename and filters into list of lowercase words"""
    with open(filename) as my_file:
        for line in my_file:
            pass

if __name__ == '__main__':
    word_list = ["bird", "calf", "river", "stream", "kneecap",  "cookbook",
                 "language", "sneaker", "algorithm", "integration", "brain"]

    main(word_list)
