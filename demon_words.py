
import mystery_word as mw

import random
import re

#length of word is decided at the beginning
#   this filters the dictionary
#word should only consist of the blanks(.) and placed letters
#available_words should consist of all words which match the current regular expression
#the placement of the guessed characters is based on maximizing the available subgroup

class DemonWord(mw.MysteryWord):
    """docstring for DemonWord"""
    def __init__(self, word_length=6):
        super(DemonWord, self).__init__()
        self.word_length = 6
        self.regexp = '.'*6


    def set_word_length(self, word_length=6):
        self.word_length = word_length

    def filter_word_list(self, word_list, regexp):
        """Regexp is any character that has been guessed or . if location is unassigned"""
        word_list = [word for word in word_list if len(word) == len(regexp)]
        regexp = ''.join(['[a-z]' if char == '.' else char for char in regexp])
        regextp = ' ' + regexp + ' '
        return re.findall(regexp, ' '.join(word_list))

    def attempt_guess(self, letter):
        """Return False if invalid, otherwise add to guesses list and return True"""
        if self.is_valid_guess(letter) == False:
            return False
        letter = letter.lower()
        word_families = self.find_word_families(self.regexp, self.word_list, letter)
        self.word_list = self.pick_word_families(word_families, letter)
        self.guesses.append(letter)

        '''
        if letter not in self.word:
            self.num_guesses_left -= 1
            print('Incorrect guess.')
        else:
            print('Correct!')
        return True
        '''
    def find_word_families(self, regexp, word_list, guess):
        word_families = {}
        family_members = []
        for word in word_list:
            if guess not in word:
                word_families[regexp] = [word]
            else:
                word_family = self.find_word_family(regexp, word, guess)
                family_members = word_families.get(word_family,[])
                family_members.append(word)
                word_families[word_family] = family_members
        return word_families

    def find_word_family(self, current_regexp, word, guess):
        """Returns a string showing which letters from letter_list are in word"""
            #assert game.find_word_family('.....', 'river', 'r') == 'r...r'
        #output_list = [self.display_regexp_char(letter, word) for letter in word]
        new_regexp = list(current_regexp)
        for slot, char  in enumerate(current_regexp):
            if word[slot] == guess:
                new_regexp[slot] = guess

        output = ''.join(new_regexp)
        return output

    def pick_word_family(self, word_families, guess='a'):
        """Picks 'hardest' word list based on word_families dictionary"""
        max = 0
        word_family = ['']

        for key, value in word_families.items():
            if len(value) > max:
                max = len(value)
                word_family = key
        return word_families[word_family]


def user_interface(spoiler=False):

    def guess_prompt():
        guess = ''
        while not game.is_valid_guess(guess):
            guess = input('Please choose a letter: ').lower()
            if not game.is_valid_guess(guess):
                print('Invalid letter, try again...')
        return guess

    def welcome_menu():
        print('Welcome to Mystery Word!')

    def word_length_menu():
        valid_choices = 'sml'
        choice = ' '
        while choice not in valid_choices:
            choice = input('Please choose word length: [S]hort [M]edium or [L]ong: ').lower()
        if choice == 's':
            game.word = '.' * random.randrange(4,7)
        if choice == 'm':
            game.word = '.' * random.randrange(6,9)
        if choice == 'l':
            game.word = '.' * random.randrange(8,12)

    def game_loop():
        while True:
            guess = guess_prompt()
            game.attempt_guess(guess)
            print(game)
            if game.check_win() is not None:
                break
    def play_again():
        y_n = input('Play again [Y/n]?').lower()
        if y_n == 'n':
            return False
        else:
            return True


    game = DemonWord()
    game.import_word_list('/usr/share/dict/words')
    welcome_menu()
    word_length_menu()
    if spoiler:
        print('The secret word is "{}""'.format(game.word))
    print('The Mystery Word contains {} letters.'.format(len(game.word)))
    print(game)
    game_loop()
    while(play_again()):
        game = DemonWords()
        game.import_word_list('/usr/share/dict/words')

        word_length_menu()
        if spoiler:
            print('The secret word is "{}'.format(game.word))
        print('The Mystery Word contains {} letters.'.format(len(game.word)))
        print(game)
        game_loop()

if __name__ == '__main__':
    user_interface(spoiler=True)
