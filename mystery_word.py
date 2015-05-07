import random

class MysteryWord(object):
    """MysteryWord object"""
    default_word_list = ["bird", "calf", "river", "stream", "kneecap",  "cookbook",
                         "language", "sneaker", "algorithm", "integration", "brain"]

    def __init__(self, word_list=default_word_list, allowed_guesses=10, difficulty='easy_words'):
        self.word_list = word_list
        self.word = self.random_word(word_list)
        self.guesses = []
        self.allowed_guesses = allowed_guesses
        self.difficulty = difficulty

    def __str__(self):
        self.display_word(self.word, self.guesses)

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

    def display_word(self, word, letter_list):
        """Returns a string showing which letters from letter_list are in word"""
        output_list = [self.display_letter(letter, letter_list) for letter in word]
        output = ' '.join(output_list)
        return output

    def display_letter(self, letter, letter_list, blank_char='_'):
        """Returns uppercase letter if letter in letter_list, else returns blank_char"""
        if letter in letter_list:
            return letter.upper()
        return blank_char

    def check_letter(letter, word, guesses):
        """Returns True if letter is in word and not in guesses
           Returns False if letter not in word nor guesses
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

    def make_guess():
        pass

game = MysteryWord()
print(game)
