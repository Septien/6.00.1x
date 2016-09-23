# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    if not lettersGuessed:
        return False
    #Indicate whether the word is in the secretWord
    lenw = len(secretWord)
    count = 0
    #Iterate over the list
    for l in secretWord:
        if l in lettersGuessed:
            count += 1
    
    if count == lenw:
        return True
    return False


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    #string containing the guessed characters so far
    guessedString = ""
    for l in secretWord:
        if l in lettersGuessed:
            guessedString += l
        else:
            guessedString += "_ "
    
    return guessedString



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    #String containing the alphabet
    string = 'abcdefghijklmnopqrstuvwxyz'
    #String containing the available letters
    avLetters = ""
    #Iterate over alphabet
    for c in string:
        if c not in lettersGuessed:
            avLetters += c
    
    return avLetters
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    #Declare and initialize necesary variables
    lettersGuessed = []
    opLeft = 8
    availableLetters = ""
    letter = ""
    guessedWord = ""
    play = True
    #Initialize game
    print ("Welcome to the game Hangman!")
    print ("I am thinking of a word that is ", len(secretWord), " letters long")
    print ("-------------")

    #Play the game
    while play:
        print ("You have ", opLeft, " guesses left")
        availableLetters = getAvailableLetters(lettersGuessed)
        print ("Available letters: ", availableLetters)
        letter = input("Please guess a letter: ")
        letter.lower()
        if letter in lettersGuessed:
            guessedWord = getGuessedWord(secretWord, lettersGuessed)
            print ("Oops! You've already guessed that letter: ", guessedWord)
        else:
            lettersGuessed += letter
            guessedWord = getGuessedWord(secretWord, lettersGuessed)
            if letter in secretWord:
                print ("Good guess: ", guessedWord)
            else:
                print ("Oops! That letter is not in my word: ", guessedWord)
                opLeft -= 1
        
        print ("------------")
        if opLeft == 0:
            print ("Sorry, you ran out of guesses. The word was ", secretWord)
            play = False
            continue
        if isWordGuessed(secretWord, lettersGuessed):
            print("Congratulations, you won!")
            play = False
            continue


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
