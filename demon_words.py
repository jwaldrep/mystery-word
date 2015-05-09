
import mystery_word as mw

import pdb
import random
import re


#length of word is decided at the beginning
#   this filters the dictionary
#word should only consist of the blanks(.) and placed letters
#available_words should consist of all words which match the current regular expression
#the placement of the guessed characters is based on maximizing the available subgroup

class DemonWord(mw.MysteryWord):
    """DemonWord class is a mystery word game which evilly dodges user guesses"""
    def __init__(self, word_length=6):
        super(DemonWord, self).__init__()
        self.word_length = 6
        self.regexp = '.'*6
        self.word = None
        self.debug_output = False
        self.hint = ''
        self.word_families = {}
        self.word_list = ['echo', 'heal', 'best', 'lazy']

    def set_word_length(self, word_length=6):
        self.word_length = word_length
        self.regexp = '.' * word_length
        self.word_list = self.filter_word_list(self.word_list, self.regexp)

    def filter_word_list(self, word_list, regexp):
        """Converts are simplified regexp to proper python regexp syntax
           Regexp consists of any character that has been correctly guessed or . if location is unassigned
        """
        word_list = [word for word in word_list if len(word) == len(regexp)]
        regexp = ''.join(['[a-z]' if char == '.' else char for char in regexp])
        regextp = ' ' + regexp + ' '
        return re.findall(regexp, ' '.join(word_list))

    def attempt_guess(self, letter):
        """Return False if invalid, otherwise add to guesses list and return True
           Because we're in evil mode, this also triggers re-evaluation of the current word list
        """
        #pdb.set_trace()
        if self.is_valid_guess(letter) == False:
            return False
        letter = letter.lower()

        old_regexp = self.regexp
        word_families = self.find_word_families(self.regexp, self.word_list, letter)
        self.word_list = self.pick_word_family(word_families, letter)
        self.guesses.append(letter)
        possible_word = self.word_list[0]
        self.regexp = self.find_word_family(self.regexp, possible_word, letter)

        if self.regexp == old_regexp:
            print('Incorrect guess.')
            self.num_guesses_left -= 1
        else:
            print('Correct!')
        return True

    def find_word_families(self, regexp, word_list, guess):
        """Given current regexp game state, the current word list, and letter guess,
            returns dictionary containing lists of words indexed by the regexp which
            would include them (if that word family is chosen)
        """
        word_families = {}
        family_members = []
        for word in word_list:
            word_family = self.find_word_family(regexp, word, guess)
            family_members = word_families.get(word_family,[])
            family_members.append(word)
            word_families[word_family] = family_members
        return word_families

    def find_word_family(self, current_regexp, word, guess):
        """Returns the regexp which would leave word in play with given guess letter"""
            #assert game.find_word_family('.....', 'river', 'r') == 'r...r'
        #output_list = [self.display_regexp_char(letter, word) for letter in word]
        new_regexp = list(current_regexp)
        if self.debug_output:
            print('current_regexp: {}, word: {}'.format(repr(current_regexp), repr(word)))
        for slot, char  in enumerate(current_regexp):
            #pdb.set_trace()
            if word[slot] == guess:
                new_regexp[slot] = guess
        output = ''.join(new_regexp)
        return output

    def pick_word_family(self, word_families, guess='a'):
        """Picks 'hardest' word list based on word_families dictionary"""
        max = 0
        word_family = ''
        if self.debug_output:
            print('word_families:{}'.format(word_families))
        for key, value in word_families.items():
            #Refactor this with a lambda
            if len(value) > max:
                max = len(value)
                word_family = key
            if self.debug_output:
                print('{},'.format(len(value)),end='')
        if self.debug_output:
            print('\nword_family: {}, return word list: {}'.format(repr(word_family), repr(word_families[word_family])))
        #consider adding check if it is the last turn to force a loss
        return word_families[word_family]

    def display_word(self):
        """Returns a string showing which letters from letter_list are in word"""
        output_list = [self.display_letter(letter) for letter in self.regexp]
        output = ' '.join(output_list)
        return output

    def is_word_complete(self):
        """Returns True if all letters in word are in letter_list"""
        for letter in self.regexp:
            if letter == '.':
                return False
        return True


def user_interface(debug_output=False):
    """Gets input from user to conduct a DemonWords game
       debug_output=True provides prints extra information about each turn
    """
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
            game.set_word_length(random.randrange(4,7))
        if choice == 'm':
            game.set_word_length(random.randrange(6,9))
        if choice == 'l':
            game.set_word_length(random.randrange(8,12))

    def game_loop():
        while True:
            guess = guess_prompt()
            game.attempt_guess(guess)
            print(game)
            if show_hints:
                print('Current word list has {} words.'.format(len(game.word_list)), end='')
            print(''.format())
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
    print('The Mystery Word contains {} letters.'.format(len(game.regexp)))
    print(game)
    if show_hints:
        print('Current word list has {} words.'.format(len(game.word_list)))

    game_loop()
    while(play_again()):
        game = DemonWord()
        game.import_word_list('/usr/share/dict/words')

        word_length_menu()
        print('The Mystery Word contains {} letters.'.format(len(game.regexp)))
        print(game)
        game_loop()

if __name__ == '__main__':
    user_interface(show_hints=True)
