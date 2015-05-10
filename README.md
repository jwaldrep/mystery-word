#Mystery Word
#####A Guessing Game with a Twist
--------



##Introduction
*Mystery Word* is the familiar word guessing game of Hangman, re-imagined for the 21st century.  Despite the kinder, gentler name, this game is not your friend.  Like nearly all modern technology, it seems hell-bent on frustrating the user, and darned if it hasn't gotten _really, really good at it._


##Getting started
### System Requirements
  * [Python 3.x.x](https://www.python.org/downloads/) (3.4.3 recommended)
  * Mac OS X (for the default word list)
Instructions
1. Clone this repository or download the files to your chosen directory and execute the following line at your command prompt:
    ```python3 demon_words.py```
    * Note: Depending on your system configuration, you may need to use ```python demon_words.py```, but be aware that [Python 3.x.x](https://www.python.org/downloads/) is required for game to run unmodified
2. Follow the prompts to choose your options as described below and then begin the game
3. At the end of each game, you may choose to play again (if you dare!) or finally admit defeat and exit the game.

##Gameplay Options

###Difficulty
Choose from the following four difficulties by entering the listed menu selection and pressing <Enter>:

Mode   | Menu Selection |Description
-----|:--------------:|-----------
Easy   | E | It almost seems like the computer is trying to help you out...
Medium | M | Just a normal hangman game where the computer picks a word and user guesses...but I hope you have a good vocabulary! I think you'll actually stand a chance here, even without the hints.
Hard   | H | Just when you thought you were getting the hang of it, the computer starts flexing its processor. You might need the hints here to make any headway here, but I promise the computer is not outright lying. If you don't believe me, check your guesses against the word after you've lost.
Evil   | V | Same as hard, but hints are misleading (suggests worst possible guess)

###Word Length
Choose from the following to select the number of letters in the mystery word:

Word Length | Menu Selection | Number of letters
------------|:--------------:|------------------
Short        | S             | 4 to 6
Medium       | M             | 6 to 8
Long         | L             | 8 to 12

###Hints
If you choose to see hints, the computer will make some gameplay suggestions...though you will have to decide for yourself if they can be trusted.



















##Developer Information:
* These modules have been tested with Python 3.4, and will not work in Python 2.x without modification
* demon_words.py is the main module for the game, while mystery_word.py is a necessary dependency
  * Nonetheless, mystery_word.py can be played as a normal hangman game, but demon_words has been designed to completely replace and extend its functionality
* The test files provided are designed for use either with nose or py.test, and as of the time of this writing all tests pass with 82% coverage on demon_words.py
* A debug mode is provided with several verbose print statements at key points in the code. This mode is activated with a command line argument like so:
    * ```python3 demon_words.py debug```
* The word list is based on `/usr/share/dict/words`, included with the stock Mac OS X Operating System
* Hard/Evil mode is based on the concept/algorithm described [here] as well as MIT's 6.00.1x course. (http://nifty.stanford.edu/2011/schwarz-evil-hangman/)

##Future Features:
* Offer to open web link definition of the Mystery Word
* More evil algorithm, especially for word list length of 2
* Option to use custom word dictionary
* Enhanced debug display
* Simple words version (1000 common english words)
* Hard/Harder modes using smaller/full size starting word lists
* Web or GUI interface
* Quick play mode for enhanced testing
* Refactor classes, and possibly make a UI class/module
* Better test coverage
* Options for alternate dictionaries on different operating systems
* Python 2 compatibility

##API
Help on DemonWord in module demon_words object:

```python
class DemonWord(mystery_word.MysteryWord)
 |  DemonWord class is a mystery word game which evilly dodges user guesses
 |  word_length is the number of letters in word to guess
 |  difficulty is 'easy'/'medium'/'hard'/'evil'
 |
 |       medium = normal hangman game, computer picks a mystery word
 |       hard = computer dodges your guesses, always maximizing the number of possible words
 |       evil = same as hard, but hints are misleading (suggests worst possible guess)
 |       easy = same AI as hard mode, but tries to maximize chance of correct guesses
 |
 |  Method resolution order:
 |      DemonWord
 |      mystery_word.MysteryWord
 |      builtins.object
 |
 |  Methods defined here:
 |
 |  __init__(self, word_length=6, difficulty='evil')
 |      Init for DemonWord class
 |
 |  attempt_guess(self, letter)
 |      Return False if invalid, otherwise add to guesses list and return True
 |      This also triggers re-evaluation of the current word_list
 |
 |  display_word(self)
 |      Returns a string showing which letters from letter_list are in word
 |
 |  filter_word_list(self, word_list, regexp)
 |      Converts our simplified regexp to proper python regexp syntax
 |      Regexp consists of any character that has been correctly guessed
 |      or '.' if location is as yet unassigned
 |
 |  find_word_families(self, regexp, word_list, guess)
 |      Given current regexp game state, the current word list, and letter guess,
 |      returns dictionary containing lists of words indexed by the regexp which
 |      would include them (if that word family is chosen)
 |
 |  find_word_family(self, current_regexp, word, guess)
 |      Returns the regexp which would leave word in play with given guess letter
 |
 |  is_word_complete(self)
 |      Returns True if all letters in word are in letter_list
 |
 |  pick_best_letter(self, lie=False)
 |      Recommend best letter for user to pick if lie=False, otherwise worst
 |
 |  pick_single_word(self)
 |      Returns a randomly selected word in self.word_list
 |
 |  pick_word_family(self, word_families, guess='a', evil=True)
 |      Picks 'hardest' word list based on word_families dictionary
 |
 |  quick_play(self, silent=False, lying_hint=False)
 |      Not yet implemented
 |
 |  set_word_length(self, word_length=6)
 |      Sets the word_length and initial blanke regexp,
 |      as well as filtering the word_list for the number of characters
 |
 |  ----------------------------------------------------------------------
 |  Methods inherited from mystery_word.MysteryWord:
 |
 |  __str__(self)
 |
 |  check_win(self)
 |      Return True for win, False for lose, None for neither
 |
 |  display_letter(self, letter)
 |      Returns uppercase letter if letter in guesses, else returns blank_char
 |
 |  easy_words(self)
 |      Returns list of words with 4-6 characters in word_list
 |
 |  hard_words(self)
 |      Returns list of words with 8+ characters in word_list
 |
 |  import_word_list(self, filename)
 |
 |  is_valid_guess(self, letter)
 |      Returns True if letter is a single letter, but not in guesses
 |
 |  medium_words(self)
 |      Returns list of words with 6-8 characters in word_list
 |
 |  random_word(self)
 |      Returns a random word from word_list
 |
 |   ----------------------------------------------------------------------
 |  Data descriptors inherited from mystery_word.MysteryWord:
 |
 |  __dict__
 |      dictionary for instance variables (if defined)
 |
 |  __weakref__
 |      list of weak references to the object (if defined)
 |
 |   ----------------------------------------------------------------------
 |  Data and other attributes inherited from mystery_word.MysteryWord:
 |
 |  default_word_list = ['bird', 'calf', 'river', 'stream', 'kneecap', 'co...
 (END)
```
