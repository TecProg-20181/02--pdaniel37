import random
import string


def constTextFile():
    return "palavras.txt"


WORDLIST_FILENAME = constTextFile()


def loadWords():
    """
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return random.choice(wordlist)


def constSecretWordImcomplete():
    return False


def constSecretWordComplete():
    return True


def isWordGuessed(secretWord, lettersGuessed):
    for letter in secretWord:
        if letter in lettersGuessed:
            pass
        else:
            response = constSecretWordImcomplete()
            return response

    response = constSecretWordComplete()
    return response


def getGuessedWord():

    guessed = ''

    return guessed


def getAvailableLetters():
    # 'abcdefghijklmnopqrstuvwxyz'
    available = string.ascii_lowercase

    return available


def constGuessesTotal():
    return 8


def constNoGuesses():
    return 0


def constGuessesDecrement():
    return -1


def hangman(secretWord):

    guesses = constGuessesTotal()
    lettersGuessed = []
    print 'Welcome to the game, Hangam!'
    print 'I am thinking of a word that is', len(secretWord), ' letters long.'
    print '-------------'

    returnFalse = constSecretWordImcomplete()
    while isWordGuessed(secretWord, lettersGuessed) == returnFalse and guesses > constNoGuesses():
        print 'You have ', guesses, 'guesses left.'

        available = getAvailableLetters()
        for letter in available:
            if letter in lettersGuessed:
                available = available.replace(letter, '')

        print 'Available letters', available
        letter = raw_input('Please guess a letter: ')
        if letter in lettersGuessed:

            guessed = getGuessedWord()
            for letter in secretWord:
                if letter in lettersGuessed:
                    guessed += letter
                else:
                    guessed += '_'

            print 'Oops! You have already guessed that letter: ', guessed
        elif letter in secretWord:
            lettersGuessed.append(letter)

            guessed = getGuessedWord()
            for letter in secretWord:
                if letter in lettersGuessed:
                    guessed += letter
                else:
                    guessed += '_'

            print 'Good Guess: ', guessed
        else:
            guesses += constGuessesDecrement()
            lettersGuessed.append(letter)

            guessed = getGuessedWord()
            for letter in secretWord:
                if letter in lettersGuessed:
                    guessed += letter
                else:
                    guessed += '_'

            print 'Oops! That letter is not in my word: ',  guessed
        print '------------'

    else:
        returnTrue = constSecretWordComplete()
        if isWordGuessed(secretWord, lettersGuessed) == returnTrue:
            print 'Congratulations, you won!'
        else:
            print 'Sorry, you ran out of guesses. The word was ', secretWord, '.'


secretWord = loadWords().lower()
hangman(secretWord)
