
import mystery_word as mw

import pdb
import random
import re
import sys


class DemonWord(mw.MysteryWord):
    """DemonWord class is a mystery word game which evilly dodges user guesses
       word_length is the number of letters in word to guess
       difficulty is 'easy'/'medium'/'hard'/'evil'

            easy = keep words in word list using guessed letter if at all possible
            medium = normal hangman game, computer picks a level
            hard = computer dodges your guesses, always maximizing the number of possible words
            evil = same as hard, but hints are misleading
    """
    def __init__(self, word_length=6, difficulty='evil'):
        """Init for DemonWord class"""
        super(DemonWord, self).__init__()
        self.word_length = 6
        self.regexp = '.'*6
        self.word = None
        self.debug_output = False
        self.hint = ''
        self.word_families = {}
        self.word_list = ['echo', 'heal', 'best', 'lazy']
        self.difficulty = difficulty
        self.current_guess = ''
        self.lying_hints = False

    def set_word_length(self, word_length=6):
        """Sets the word_length and initial blanke regexp,
           as well as filtering the word_list for the number of characters
        """
        self.word_length = word_length
        self.regexp = '.' * word_length
        self.word_list = self.filter_word_list(self.word_list, self.regexp)

    def filter_word_list(self, word_list, regexp):
        """Converts our simplified regexp to proper python regexp syntax
           Regexp consists of any character that has been correctly guessed
           or '.' if location is as yet unassigned
        """
        word_list = [word for word in word_list if len(word) == len(regexp)]
        regexp = ''.join(['[a-z]' if char == '.' else char for char in regexp])
        regextp = ' ' + regexp + ' '
        return re.findall(regexp, ' '.join(word_list))

    def attempt_guess(self, letter):
        """Return False if invalid, otherwise add to guesses list and return True
           This also triggers re-evaluation of the current word_list
        """
        if self.difficulty == 'easy':  #irrelevant in medium/normal mode
            evil = False
        else:
            evil = True
        #pdb.set_trace()
        if self.is_valid_guess(letter) == False:
            return False
        letter = letter.lower()

        old_regexp = self.regexp
        self.word_families = self.find_word_families(self.regexp, self.word_list, letter)
        self.word_list = self.pick_word_family(self.word_families, letter, evil)
        self.guesses.append(letter)
        possible_word = self.word_list[0]
        self.regexp = self.find_word_family(self.regexp, possible_word, letter)

        if self.regexp == old_regexp:
            print('Incorrect guess.\n')
            self.num_guesses_left -= 1
        else:
            print('Correct!\n')

        if self.check_win() == False:
            self.word = self.pick_single_word() #The final lie

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

    def pick_word_family(self, word_families, guess='a', evil=True):
        """Picks 'hardest' word list based on word_families dictionary"""
        max = 0
        word_family = ''
        if (not evil) and len(word_families) > 1:
            #print('word_families: {}'.format(word_families))
            if self.current_guess in ''.join(word_families): #if guessed letter is somewhere in the keys
                try:
                    temp = word_families[self.regexp]
                    del(word_families[self.regexp])   #remove incorrect guesses as an option
                except:
                    #word_families[self.regexp] = temp
                    pass  #Dirty hack for bug with easy, long, 'q', 'u' -- index out of range
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

    def pick_best_letter(self, lie=False):
        """Recommend best letter for user to pick if lie=False, otherwise worst"""
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        available = [letter for letter in alphabet if letter not in self.guesses]
        letter_scores = {}

        def simple_pick():
            """Just pick a letter based on letters known to be in word_list words"""
            word_list_set = set(''.join(self.word_list)) #removes duplicates
            available_hits = [letter for letter in available if letter in word_list_set]
            self.hint = random.choice(available_hits)

        if len(self.word_list) < 3:
            simple_pick()
            return

        for letter in available:
            ##word_families = self.find_word_families(self.regexp, self.word_list, letter)
            ##print('word_families: {}'.format(self.word_families))
            ##letter_scores[letter] = ([word_families[x] for x in word_families])
            #possible_word = self.word_list[0]
            #potential_regexp = self.find_word_family(self.regexp, possible_word, letter)
            #potential_wordlist = self.filter_word_list(self.word_list, potential_regexp)
            #letter_scores[letter] = len(potential_wordlist)
            potential_word_families = self.find_word_families(self.regexp, self.word_list, letter)
            potential_word_list = self.pick_word_family(potential_word_families, letter)
            #possible_word = potential_word_list[0]
            #possible_regexp = self.find_word_family(self.regexp, possible_word, letter)

            letter_scores[letter] = potential_word_list
        if self.debug_output:
            print('letter scores: {}'.format([len(letter_scores[x]) for x in letter_scores]))


        try:
            min_score = min([len(letter_scores[letter]) for letter in available if letter in ''.join(letter_scores[letter])])
            max_score = max([len(letter_scores[letter]) for letter in available if letter not in ''.join(letter_scores[letter])])

        except:
            min_score = min([len(letter_scores[letter]) for letter in available])
            max_score = max([len(letter_scores[letter]) for letter in available])

        if (max_score == 1 and lie==True) or (min_score == 1 and lie == False):
            simple_pick()
            return

        for letter in letter_scores:
            if lie==True and len(letter_scores[letter]) == max_score:
                self.hint = letter

            elif lie==False and len(letter_scores[letter]) == min_score:
                self.hint = letter


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

    def pick_single_word(self):
        """Returns a randomly selected word in self.word_list"""
        return random.choice(self.word_list)

    def quick_play(self, silent=False, lying_hint=False):
        """Not yet implemented"""
        pass
        '''
        for _ in range(self.num_guesses_left):
            letter = self.pick_best_letter(lie=lying_hint)
            if not silent:
                print('You guessed {}'.format(letter))
            self.attempt_guess(letter)
            if not silent:
                print(self)
            if self.check_win() is not None:
                break
        '''


def user_interface(show_hint=False, lying_hints=False, show_debug_output=False):
    """Gets input from user to conduct a DemonWords game
       show_hint=True shows hints at each turn (this will be overridden by user menu)
       lying_hints=True shows hints that make it harder to win (may be overriden by user menu)
       debug_output=True provides prints extra information about each turn (may be overriden by command prompt options)
    """
    def guess_prompt():
        guess = ''
        while not game.is_valid_guess(guess):
            guess = input('Please choose a letter: ').lower()
            if not game.is_valid_guess(guess):
                print('Invalid letter, try again...')
        game.current_guess = guess
        return guess

    def welcome_menu():
        print('Welcome to Mystery Word!')
        print("Please select from the following options.")

    def select_difficulty_menu():
        game.difficulty = one_key_menu(choices={'e': 'easy', 'm': 'medium', 'h': 'hard', 'v': 'evil'},
                            prompt='Choose a difficulty level -- [E]asy, [M]edium, [H]ard, e[V]il: ',
                            default='m',
                            force_compliance=True,
                            force_msg='Please choose from the listed options, or q to exit.',
                            exit_words=['q','quit','end','exit'])

    def choose_hints_menu():
        return one_key_menu(choices={'y': True, 'n': False},
                            prompt='Would you like friendly hints? [y/N] : ',
                            default='n',
                            force_compliance=False,
                            force_msg='',
                            exit_words=['q','quit','end','exit'])


    def word_length_menu():
        valid_choices = 'sml'
        choice = ' '
        while (choice not in valid_choices) or choice == '':
            choice = input('Please choose word length: [S]hort [M]edium or [L]ong: ').lower()
        if choice == 's':
            game.set_word_length(random.randrange(4,7))
        if choice == 'm':
            game.set_word_length(random.randrange(6,9))
        if choice == 'l':
            game.set_word_length(random.randrange(8,12))
        ###Move these elsewhere, if possible:
        if game.difficulty == 'medium':

            game.word = random.choice([x for x in game.word_list if len(x) == game.word_length])
            game.word_list = [game.word]

        if game.difficulty == 'evil':
            game.lying_hints = True

    def game_loop():
        while True:
            guess = guess_prompt()
            game.attempt_guess(guess)
            print(game)
            if show_hint:
                show_hints()
            if game.check_win() is not None:
                break

    def play_again():
        return one_key_menu(choices={'y': True, 'n': False},
                            prompt='Play again [Y/n]?',
                            default='y',
                            force_compliance=False,
                            force_msg='',
                            exit_words=['q','quit','end','exit'])

    def show_hints():
        if game.check_win() is None:
            game.pick_best_letter(game.lying_hints)
            s = 's' if len(game.word_list) > 1 else ''
            print('Current word list has {} word{}.  '.format(len(game.word_list), s), end='')
            print("Might I recommend you try '{}'?\n".format(game.hint))

    def one_key_menu(choices={'y': True, 'n': False} , prompt='Y/n?', default='y', force_compliance=False, force_msg='Please try again. \n', exit_words=['quit','end','exit']):
        """Function for capturing case-insensitive single letter input
           Probably could also be used for >1 letter input with a list input into acceptable

           choices is an iterable that contains all valid input options, must be all lowercase
           prompt is the text to display on the line taking input
           default is the value to choose on blank or bogus input, must be lowercase
           force_compliance set to True loops the input prompt until an acceptable answer is met
           force_msg is a message to display on improper input, including newlines if needed
           exit_words contains allowed input for exiting the loop, must be lowercase
        """
        kb_input = input(prompt).lower()
        if kb_input in exit_words:
            sys.exit('Exiting game by user request.')

        if kb_input not in choices:
            if force_compliance:
                print(force_msg)
                return one_key_menu()
            else:
                return default
        else:
            return choices[kb_input]

    game = DemonWord()
    game.debug_ouput = show_debug_output
    game.import_word_list('/usr/share/dict/words')
    if game.debug_output:
        game.word_list = game.word_list[:1000]
    welcome_menu()
    select_difficulty_menu()
    word_length_menu()
    show_hint = choose_hints_menu()
    print('The Mystery Word contains {} letters.'.format(len(game.regexp)))
    print(game)
    if show_hint:
        show_hints()
    game_loop()
    while(play_again()):
        game = DemonWord()
        game.import_word_list('/usr/share/dict/words')
        if game.debug_output:
            game.word_list = game.word_list[:1000]
        select_difficulty_menu()
        word_length_menu()
        show_hint = choose_hints_menu()
        print('The Mystery Word contains {} letters.'.format(len(game.regexp)))
        print(game)
        if show_hint:
            show_hints()
        game_loop()

if __name__ == '__main__':
    """Use 'debug' command line option to enter debug mode"""
    to_debug = False
    try:
        if len(sys.argv) > 1 and sys.argv[1] == 'debug':
            to_debug = True
            print('Running in debug mode...')
    except:
        pass
    user_interface(show_hint=True, lying_hints=False, show_debug_output=to_debug)
