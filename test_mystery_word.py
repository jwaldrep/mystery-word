import mystery_word as mw

game = mw.MysteryWord()
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

game.word_list = ["bird", "calf", "river", "stream", "kneecap",  "cookbook",
             "language", "sneaker", "algorithm", "integration", "brain"]


def test_easy_words():
    assert game.easy_words() == \
        ["bird", "calf", "river", "stream", "brain"]


def test_medium_words():
    assert MysteryWord.medium_words(word_list) == \
        ["stream", "kneecap", "cookbook", "language", "sneaker"]


def test_hard_words():
    assert MysteryWord.hard_words(word_list) == \
        ["cookbook", "language", "algorithm", "integration"]


def test_random_word():
    """This test is not very good. Testing things that are random is hard, in
    that there's not a predictable choice. The best we can do is make sure
    we have valid output."""
    word = MysteryWord.random_word(word_list)
    assert word in word_list


def test_display_word():
    word = "integration"
    assert MysteryWord.display_word(word, []) == "_ _ _ _ _ _ _ _ _ _ _"
    assert MysteryWord.display_word(word, ["z"]) == "_ _ _ _ _ _ _ _ _ _ _"
    assert MysteryWord.display_word(word, ["g"]) == "_ _ _ _ G _ _ _ _ _ _"
    assert MysteryWord.display_word(word, ["i"]) == "I _ _ _ _ _ _ _ I _ _"
    assert MysteryWord.display_word(word, ["i", "g"]) == "I _ _ _ G _ _ _ I _ _"
    assert MysteryWord.display_word(word, ["i", "n", "z"]) == "I N _ _ _ _ _ _ I _ N"


def test_is_word_complete():
    word = "river"
    assert not MysteryWord.is_word_complete(word, [])
    assert not MysteryWord.is_word_complete(word, ["r"])
    assert not MysteryWord.is_word_complete(word, ["r", "e"])
    assert not MysteryWord.is_word_complete(word, ["r", "e", "z"])
    assert MysteryWord.is_word_complete(word, ["r", "e", "v", "i"])
