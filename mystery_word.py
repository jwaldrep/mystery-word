import random


def easy_words(word_list):
    """Returns list of words with 4-6 characters in word_list"""
    return [word for word in word_list if 4 <= len(word) <= 6]

def medium_words(word_list):
    """Returns list of words with 6-8 characters in word_list"""
    return [word for word in word_list if 6 <= len(word) <= 8]

def hard_words(word_list):
    """Returns list of words with 8+ characters in word_list"""
    return [word for word in word_list if 8 <= len(word)]

def random_word(word_list):
    """Returns a random word from word_list"""
    return random.choice(word_list)

def display_word(word, letter_list):
    """Returns a string showing which letters from letter_list are in word"""
    output_list = [display_letter(letter, letter_list) for letter in word]
    output = ' '.join(output_list)
    return output

def display_letter(letter, letter_list, blank_char='_'):
    """Returns uppercase letter if letter in letter_list, else returns blank_char"""
    if letter in letter_list:
        return letter.upper()
    return blank_char

def check_letter(letter, word, guesses):
    """Returns True if letter is in word and not in guesses
       Returns False if letter not in words nor guesses
       Returns None if letter already in guesses
    """
    if letter in word and letter not in guesses:
        return True
    if letter in guesses:
        return None
    return False

def is_word_complete(word, letter_list):
    """Returns True if all letters in word are in letter_list"""
    for letter in word:
        if letter not in letter_list:
            return False
    return True
