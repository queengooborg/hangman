#
# Mike Glover
# mglover@pobox.com
# 
# Hangman
# Interactive hangman console game for 1 or 2 players
# 
# written for Intro to Programming
# Village Home, Winter 2013
#

# python 2 compatibility
try:
    raw_input
except NameError:
    # python 3
    def output(msg='', end='\n'):
        print(msg, end=end)
else:
    # python 2
    input = raw_input
    def output(msg='', end='\n'):
        print (msg+end),

        


import levels
import dictionaries


DASH = '_'

def getInt(prompt, min, max):
    """Prompt the user for an integer
    between min and max, inclusive
    """
    ret = None
    while not ret or ret<min or ret>max:
        try:
            ret = int(input("%s (%d-%d)? " % (prompt, min, max)))
        except ValueError:
            output("That isn't a number!!")
        if ret < min:
            output("That number is too small!")
        elif ret > max:
            output("That's too big!")
    return ret 

def getMenuChoice(prompt, choices, label_func):
    """Prompt the user to choose one from a list of options
    """
    choice = None

    while not choice:
        output(prompt)
        for i in range(len(choices)):
            output("[%d] %s" % (i+1, label_func(choices[i])))
        num = input('Your Choice(1-%d): ' % (len(choices)))
        try:
            choice = choices[int(num)-1]
        except(ValueError, IndexError):
            output("I didn't understand that!")

    return choice



class Hangman(object):
    def __init__(self):
        self.players = 0
        self.chooser = None
        self.guesser = None
        self.winner = None
        
        self.level = None
        
        self.word = ''        
        self.hits = ''
        self.misses = ''

        self.message = ''

    @classmethod
    def fromUserInput(cls):
        """ Create a new Hangman class and fill in values based on 
        user input from the keyboard.
        """
        
        obj = cls()
        
        output("Welcome to Hangman!")
        output()

        obj.players = getInt("How many players", 1, 2)
    
        if obj.players == 2:
            obj.chooser = input("Who will choose the word? ")
            obj.guesser = input("Who will guess the word? ")
            obj.userWord()

        else:
            obj.guesser = input("What is your name? ")
            obj.chooser = "Computer"
            obj.randomWord()

        all_levels = levels.getLevels()
        obj.level = getMenuChoice("What level would you like to play?",
                                  all_levels, 
                                  lambda l: "%s: (%d chances)"%(l.description,
                                                                l().misses))()
        return obj

    def reset(self):
        self.winner = None
        self.hits = ''
        self.misses = ''

		# XXX in multiplayer mode, 2 or more
		# XXX players might use a random word
        if self.players == 1:
            self.randomWord()
        else:
            new_chooser = input("Who will choose the next word, %s or %s?"
                                    %(self.guesser, self.chooser))
            while new_chooser not in (self.guesser, self.chooser):
                new_chooser = input(
                    "Who will choose the next word, %s or %s?"
                    %(self.guesser, self.chooser))
            if new_chooser != self.chooser:
                self.guesser = self.chooser
                self.chooser = new_chooser
            self.userWord()

    def clearScreen(self):
        # XXX we can do a better job than this!
        for i in range(35):
            output()

    def randomWord(self, dictionary=None):
        """ Randomly choose a word from the given dictionary
        """
        dictionary = getMenuChoice("What kind of word shall I use?",
                                   dictionaries.getDicts(),
                                   lambda x: x.name)
        self.word = dictionary.randomWord()

    def userWord(self):
        output("OK.  Close your eyes, %s." % (self.guesser), end=' ')
        output("It's time for %s to choose the word." % self.chooser)
        input ("Press the enter key when you're ready, %s" % self.chooser)

        self.word = input ("Type the word: ")
        while not self.word.isalpha():
            output("The word can only have letters, ", end=' ')
            output("no numbers, spaces, or punctuation.")
            self.word = input ("Type the word: ")
        input ("Got it. Press the enter key to continue.")
        self.clearScreen()

    def printGallows(self):
        output(self.level.gallows(len(self.misses)))

    def printWordDashes(self):
        output("Word: ", end=' ')
        for letter in self.word:
            if letter in self.hits:
                output(letter.upper(), end=' ')
            else:
                output(DASH, end=' ')
            output(" ", end=' ')
        output()

    def printMisses(self):
        output("Letters guessed: ", end=' ')
        for letter in self.misses:
            output(letter.upper(), end=' ')
        output()
            
    def printResult(self):
        assert self.winner is not None, "no winner"

        self.clearScreen()
        self.printGallows()
        output("Congratulations, %s!" % self.winner)
        output()
        output("The word was: %s" % self.word.upper())


    def printMessage(self):
        output(self.message)
        self.message = ''

    def play(self):
        """Play one round of hangman
        """
        self.clearScreen()
        self.printGallows()
        self.printWordDashes()
        self.printMisses()
        self.printMessage()
        
        letter = input("Guess a letter, %s: " % self.guesser)
        while len(letter) != 1 or not letter.isalpha():
            output("That isn't a letter!")
            letter = input("Guess a letter, %s: " % self.guesser)

        if letter in self.hits or letter in self.misses:
            self.message = "You already guessed that!"

        elif letter in self.word:
            self.hits += letter
        else:
            self.misses += letter
            
        if len(self.misses) >= game.level.misses:
            # out of guesses
            self.winner = self.chooser

        if set(self.word) == set(self.hits):
            # all letters have been guessed
            self.winner = self.guesser
        

if __name__ == '__main__':
    game = Hangman.fromUserInput()
    done = False

    while not done:

        # play a game
        while not game.winner:
            game.play()
        game.printResult()
        
        # play again without re-entering names, etc.
        again = input("Play again (Y/n)? ")
        if again.upper() != 'N':
            game.reset()
        else:
            done = True
