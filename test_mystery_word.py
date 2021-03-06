import mystery_word as mw

game = mw.MysteryWord()

game.word_list = ["bird", "calf", "river", "stream", "kneecap",  "cookbook",
             "language", "sneaker", "algorithm", "integration", "brain"]


def test_easy_words():
    assert game.easy_words() == \
        ["bird", "calf", "river", "stream", "brain"]


def test_medium_words():
    assert game.medium_words() == \
        ["stream", "kneecap", "cookbook", "language", "sneaker"]


def test_hard_words():
    assert game.hard_words() == \
        ["cookbook", "language", "algorithm", "integration"]


def test_random_word():
    """This test is not very good. Testing things that are random is hard, in
    that there's not a predictable choice. The best we can do is make sure
    we have valid output."""
    word = game.random_word()
    assert word in game.word_list


def test_display_word():
    game = mw.MysteryWord()
    game.word = "integration"

    assert game.display_word() == "_ _ _ _ _ _ _ _ _ _ _"

    game.attempt_guess('z')
    assert game.display_word() == "_ _ _ _ _ _ _ _ _ _ _"

    game.attempt_guess('g')
    assert game.display_word() == "_ _ _ _ G _ _ _ _ _ _"

    game.guesses = []
    game.attempt_guess('i')
    assert game.display_word() == "I _ _ _ _ _ _ _ I _ _"

    game.attempt_guess('g')
    assert game.display_word() == "I _ _ _ G _ _ _ I _ _"

    game.guesses.remove('g')
    game.attempt_guess('n')
    assert game.display_word() == "I N _ _ _ _ _ _ I _ N"

    game.attempt_guess('z')
    assert game.display_word() == "I N _ _ _ _ _ _ I _ N"



def test_is_word_complete():
    game = mw.MysteryWord()
    game.word = "river"

    game.guesses = ["r"]
    assert not game.is_word_complete()

    game.guesses = ["r", "e"]
    assert not game.is_word_complete()

    game.guesses = ["r", "e", "z"]
    assert not game.is_word_complete()

    game.guesses = ["r", "e", "v", "i"]
    assert game.is_word_complete()

def test_winning_game():
    game = mw.MysteryWord()
    game.word = 'landuade'
    game.quick_play(letters_to_guess='rstlneaioubcdfghjkmpqvwxyz')
    assert game.check_win() == True
    assert game.num_guesses_left == 1

def test_losing_game():
    game = mw.MysteryWord()
    game.word = 'carbong'
    game.quick_play(letters_to_guess='rstlneaioubcdfghjkmpqvwxyz')
    assert game.check_win() == False
    assert game.num_guesses_left == 0

def test_invalid_guesses():
    game = mw.MysteryWord()
    game.word = 'calf'

    game.attempt_guess('x')
    assert game.num_guesses_left == 7

    game.attempt_guess('c')
    assert game.num_guesses_left == 7

    game.attempt_guess('c')
    assert game.num_guesses_left == 7

    game.attempt_guess('C')
    assert game.num_guesses_left == 7

    game.attempt_guess('.')
    assert game.num_guesses_left == 7

    game.attempt_guess('a')
    assert game.num_guesses_left == 7

    game.attempt_guess('d')
    assert game.num_guesses_left == 6

    game.attempt_guess(' ')
    assert game.num_guesses_left == 6
