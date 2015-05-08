import demon_words as dw
import pdb

game = dw.DemonWord()

game.word_list = ["bird", "calf", "river", "stream", "kneecap",  "cookbook",
             "language", "sneaker", "algorithm", "integration", "brain"]


def test_filter_word_list():
    filtered = game.filter_word_list(game.word_list, regexp='.'*5) #[a-z][a-z][a-z][a-z][a-z]')

    assert filtered == ["river", "brain"]

def test_find_word_family():
    assert game.find_word_family('.....', 'river', 'r') == 'r...r'

def test_find_word_families():
    word_list = ['lazy']
    assert game.find_word_families('....', word_list, 'e') == {'....': ['lazy']}
    word_list = ['echo', 'heal', 'best', 'lazy']
    #pdb.set_trace()
    assert game.find_word_families('....', word_list, 'e') == {
        'e...': ['echo'],
        '....': ['lazy'],
        '.e..': ['heal', 'best']
        }


'''
def find_word_family(self, current_regexp, word, letter):
    """Returns a string showing which letters from letter_list are in word"""
    output_list = [self.display_regexp_char(letter) for letter in self.regexp]
    output = ' '.join(output_list)
    return output

def display_regexp_char(self, letter, word):
    """Returns lowercase letter if letter in guesses, else returns blank_char"""
    if letter in word:
        return letter.lower()
    return '.'
'''
