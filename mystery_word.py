import random

class MysteryWord(object):
    """MysteryWord object"""
    default_word_list = ["bird", "calf", "river", "stream", "kneecap",  "cookbook",
                         "language", "sneaker", "algorithm", "integration", "brain"]

    def __init__(self, word_list=default_word_list, allowed_guesses=10, difficulty='easy_words'):
        self.word_list = word_list
        self.word = self.random_word(word_list)
        self.guesses = []
        self.num_guesses_left = allowed_guesses
        self.difficulty = difficulty
        self.blank_char = '_'

    def __str__(self):
        output = self.display_word()
        es = '' if self.num_guesses_left == 1 else 'es'
        output += '\n{} guess{} left.'.format(self.num_guesses_left, es)
        if self.check_win() == True:
            output += '\nYou win!'
        if self.check_win() == False:
            output += '\nYou lose!'
        return output

    def easy_words(self, word_list):
        """Returns list of words with 4-6 characters in word_list"""
        return [word for word in word_list if 4 <= len(word) <= 6]

    def medium_words(self, word_list):
        """Returns list of words with 6-8 characters in word_list"""
        return [word for word in word_list if 6 <= len(word) <= 8]

    def hard_words(self, word_list):
        """Returns list of words with 8+ characters in word_list"""
        return [word for word in word_list if 8 <= len(word)]

    def random_word(self, word_list):
        """Returns a random word from word_list"""
        return random.choice(word_list)

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

    def is_word_complete(self, word, letter_list):
        """Returns True if all letters in word are in letter_list"""
        for letter in word:
            if letter not in letter_list:
                return False
        return True

    def attempt_guess(self, letter):
        """Return False if invalid, otherwise add to guesses list and return True"""
        if self.is_valid_guess(letter) == False:
            return False
        self.guesses.append(letter)
        if letter not in self.word:
            self.num_guesses_left -= 1
        return True

    def check_win(self):
        """Return True for win, False for lose, None for neither"""
        if self.is_word_complete(self.word, self.guesses):
            return True
        if self.num_guesses_left < 1:
            return False
        return None

game = MysteryWord()
#game.word = 'calf'
#game.num_guesses_left = 11
print('The secret word is "{}""'.format(game.word))

for letter in 'rstlneaioubcdfghjkmpqvwxyz':
    print('You guessed {}'.format(letter))
    game.attempt_guess(letter)
    print(game)
    if game.check_win() is not None:
        break

#using above string for guesses
#'language','cold': win with 1 guess left'
#'calf': lose with 10 turns, win with 11
