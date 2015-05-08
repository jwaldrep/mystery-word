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
    assert game.find_word_family('.....', 'river', 'x') == '.....'
    assert game.find_word_family('r...r', 'river', 'v') == 'r.v.r'
    assert game.find_word_family('r...r', 'river', 'x') == 'r...r'
    assert game.find_word_family('river', 'river', 'i') == 'river'

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
def test_pick_word_family():
    word_list = ['echo', 'heal', 'best', 'lazy']
    #pdb.set_trace()
    word_families = game.find_word_families('....', word_list, 'e')
    for _ in range(100):
        assert game.pick_word_family(word_families, 'e') == ['heal', 'best']

def test_set_word_length():
    game = dw.DemonWord()
    game.set_word_length(4)
    assert game.regexp == '....'

def test_attempt_guess():
    game = dw.DemonWord()
    game.set_word_length(4)
    game.word_list = ['echo', 'heal', 'best', 'lazy']
    game.attempt_guess('e')
    assert self.regexp == '.e..'

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
