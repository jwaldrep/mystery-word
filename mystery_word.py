import random

class MysteryWord(object):
    """MysteryWord object"""
    default_word_list = ["bird", "calf", "river", "stream", "kneecap",  "cookbook",
                         "language", "sneaker", "algorithm", "integration", "brain"]

    def __init__(self, word_list=default_word_list, allowed_guesses=10, difficulty='easy_words'):
        self.word_list = word_list
        self.word = self.random_word()
        self.guesses = []
        self.num_guesses_left = allowed_guesses
        self.difficulty = difficulty
        self.blank_char = '_'

    def __str__(self):
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        available = [letter.upper() for letter in alphabet if letter not in self.guesses]
        output = self.display_word()
        es = '' if self.num_guesses_left == 1 else 'es'
        output += '\n{} guess{} left.'.format(self.num_guesses_left, es)
        output += '\nAvailable Letters: {}'.format(' '.join(available))
        if self.check_win() == True:
            output += '\nYou win!'
        if self.check_win() == False:
            output += '\nYou lose! The Mystery Word was "{}"'.format(self.word)
        return output

    def import_word_list(self, filename):
        self.word_list = []
        with open(filename) as fn:
            for line in fn:
                self.word_list.append(line.strip().lower())

    def easy_words(self):
        """Returns list of words with 4-6 characters in word_list"""
        return [word for word in self.word_list if 4 <= len(word) <= 6]

    def medium_words(self):
        """Returns list of words with 6-8 characters in word_list"""
        return [word for word in self.word_list if 6 <= len(word) <= 8]

    def hard_words(self):
        """Returns list of words with 8+ characters in word_list"""
        return [word for word in self.word_list if 8 <= len(word)]

    def random_word(self):
        """Returns a random word from word_list"""
        return random.choice(self.word_list)

    def display_word(self):
        """Returns a string showing which letters from letter_list are in word"""
        output_list = [self.display_letter(letter) for letter in self.word]
        output = ' '.join(output_list)
        return output

    def display_letter(self, letter):
        """Returns uppercase letter if letter in guesses, else returns blank_char"""
        if letter in self.guesses:
            return letter.upper()
        return self.blank_char

    def is_valid_guess(self, letter):
        """Returns True if letter is a single letter, but not in guesses"""
        if letter not in self.guesses and len(letter) == 1 and letter.isalpha():
            return True
        return False

    def is_word_complete(self):
        """Returns True if all letters in word are in letter_list"""
        for letter in self.word:
            if letter not in self.guesses:
                return False
        return True

    def attempt_guess(self, letter):
        """Return False if invalid, otherwise add to guesses list and return True"""
        if self.is_valid_guess(letter) == False:
            return False
        letter = letter.lower()
        self.guesses.append(letter)
        if letter not in self.word:
            self.num_guesses_left -= 1
        return True

    def check_win(self):
        """Return True for win, False for lose, None for neither"""
        if self.is_word_complete():
            return True
        if self.num_guesses_left < 1:
            return False
        return None

    def quick_play(self, silent=False, letters_to_guess='rstlneaioubcdfghjkmpqvwxyz'):
        if not silent:
            print('The secret word is "{}""'.format(self.word))
        for letter in letters_to_guess:
            if not silent:
                print('You guessed {}'.format(letter))
            self.attempt_guess(letter)
            if not silent:
                print(self)
            if self.check_win() is not None:
                break

def user_interface(spoiler=False):

    def guess_prompt():
        guess = ''
        while not game.is_valid_guess(guess):
            guess = input('Please choose a letter: ').lower()
        return guess

    def welcome_menu():
        print('Welcome to Mystery Word!')

    def word_length_menu():
        valid_choices = 'sml'
        choice = ' '
        while choice not in valid_choices:
            choice = input('Please choose word length: [S]hort [M]edium or [L]ong: ').lower()
        if choice == 's':
            game.word = random.choice(game.easy_words())
        if choice == 'm':
            game.word = random.choice(game.medium_words())
        if choice == 'l':
            game.word = random.choice(game.hard_words())

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

    word_length = 'easy'
    difficulty = 'easy'

    game = MysteryWord()
    game.import_word_list('/usr/share/dict/words')
    welcome_menu()
    word_length_menu()
    if spoiler:
        print('The secret word is "{}""'.format(game.word))
    print('The Mystery Word contains {} letters.'.format(len(game.word)))
    print(game)
    game_loop()
    while(play_again()):
        game = MysteryWord()
        game.import_word_list('/usr/share/dict/words')

        word_length_menu()
        if spoiler:
            print('The secret word is "{}""'.format(game.word))
        print('The Mystery Word contains {} letters.'.format(len(game.word)))
        print(game)
        game_loop()

if __name__ == '__main__':
    user_interface(spoiler=True)
