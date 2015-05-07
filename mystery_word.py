import random


def easy_words(word_list):
    return [word for word in word_list if 4 <= len(word) <= 6]

def medium_words(word_list):
    return [word for word in word_list if 6 <= len(word) <= 8]

def hard_words(word_list):
    return [word for word in word_list if 8 <= len(word)]

def random_word(word_list):
    return random.choice(word_list)

def display_word(word, word_list):
    pass

def is_word_complete(word, letter_list):
    for letter in word:
        if letter not in letter_list:
            return False
    return True
