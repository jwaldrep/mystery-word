from mystery_word import *

def main(starting_word_list):
    word_list = choose_difficulty(starting_word_list)
    print(word_list)



def choose_difficulty(starting_word_list):
    """Asks user for difficulty level and passes appropriate word list function"""
    levels = {'E': easy_words, 'N': medium_words, 'H': hard_words}
    selection = ''
    while selection not in levels:
        selection = input('Please choose [E]asy, [N]ormal, or [H]ard mode: ').upper()
    level = levels[selection]
    return level(starting_word_list)

def get_starting_word_list(filename='/usr/share/dict/words'):
    """Takes filename and filters into list of lowercase words"""
    pass

if __name__ == '__main__':
    word_list = ["bird", "calf", "river", "stream", "kneecap",  "cookbook",
                 "language", "sneaker", "algorithm", "integration", "brain"]

    main(word_list)
