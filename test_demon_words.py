import demon_words as dw
import pdb

game = dw.DemonWord()

game.word_list = ["bird", "calf", "river", "stream", "kneecap",  "cookbook",
             "language", "sneaker", "algorithm", "integration", "brain"]

def test_setup():
    game = dw.DemonWord()

def test_filter_word_list():
    test_setup()
    filtered = game.filter_word_list(game.word_list, regexp='.'*5) #[a-z][a-z][a-z][a-z][a-z]')

    assert filtered == ["river", "brain"]

def test_find_word_family():
    test_setup()
    assert game.find_word_family('.....', 'river', 'r') == 'r...r'
    assert game.find_word_family('.....', 'river', 'x') == '.....'
    assert game.find_word_family('r...r', 'river', 'v') == 'r.v.r'
    assert game.find_word_family('r...r', 'river', 'x') == 'r...r'
    assert game.find_word_family('river', 'river', 'i') == 'river'

def test_find_word_families():
    test_setup()
    word_list = ['lazy']
    assert game.find_word_families('....', word_list, 'e') == {'....': ['lazy']}
    word_list = ['echo', 'heal', 'best', 'lazy']
    #pdb.set_trace()
    assert game.find_word_families('....', word_list, 'e') == {
        'e...': ['echo'],
        '....': ['lazy'],
        '.e..': ['heal', 'best']
        }
    word_list = ['echo', 'heal', 'best', 'lazy']
    #pdb.set_trace()
    assert game.find_word_families('....', word_list, 'z') == {
        '....': ['echo', 'heal', 'best'],
        '..z.': ['lazy'],
        }

def test_pick_word_family():
    test_setup()
    word_list = ['echo', 'heal', 'best', 'lazy']
    #pdb.set_trace()
    word_families = game.find_word_families('....', word_list, 'e')
    for _ in range(100):
        assert game.pick_word_family(word_families, 'e') == ['heal', 'best']


def test_set_word_length():
    test_setup()
    game.set_word_length(4)
    assert game.regexp == '....'

def test_attempt_guess():
    test_setup()
    game.set_word_length(4)
    game.word_list = ['echo', 'heal', 'best', 'lazy']
    game.attempt_guess('e')
    assert game.regexp == '.e..'

def test_pick_best_letter():
    test_setup()
    game.word_list = ['echo', 'heal', 'best', 'lazy']
    game.attempt_guess('x')
    for _ in range(1000):
        game.pick_best_letter(lie=False)
        assert game.hint in 'hal'
        #may need better test here

def test_pick_best_letter_no_lie():
    test_setup()
    game.word_list = ['heal', 'herd', 'hers']
    game.guesses = [x for x in 'abcdefghijklmnopqrstuvwxyz' if x not in 'herdalsq']
        #    game.word_list = ['heal', 'herd', 'hers'] # x not in herdals
        #WRONG WAY OF THINKING (Common Letters): h:3, e:3, r:2, d:1, a:1, l:1, s:1
        #(longest wordlist for any regexp from letter, starting with regexp='....'
        #so right way is: h:3>0x e:3>0x r:2>1x d:2x>1 a:2x>1 l:2x>1 s:2x>1 q:3>0x
        #(x=....)

        #    game.word_list = ['heal', 'herd', 'hers'] # x not in herdls
        #h:3>0x e:3>0x r:3>0x d:2x>1 l:2x>1 s:2x>1
    for _ in range(1000):
        game.pick_best_letter(lie=False)
        assert game.hint in 'rdals'


def test_pick_best_letter_lie():
    test_setup()
    game.word_list = ['heal', 'herd', 'hers']
    game.guesses = [x for x in 'abcdefghijklmnopqrstuvwxyz' if x not in 'herdalsq']
    for _ in range(1000):
        game.pick_best_letter(lie=True)
        assert game.hint in 'heq'

def test_pick_best_letter_last_word():
    test_setup()
    game.word_list = ['heal']
    game.guesses = [x for x in 'abcdefghijklmnopqrstuvwxyz' if x not in 'heal']
    for _ in range(1000):
        game.pick_best_letter(lie=False)
        assert game.hint in 'heal'


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
