# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
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
    # FILL IN YOUR CODE HERE...
    
    testcount=0
    for char in secretWord:
        if char in lettersGuessed:
            testcount+=1
    if testcount==len(secretWord):
        return True
    else:
        return False
            
    


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    ## how the word will display:
    displayWord = str('_ /')*len(secretWord)
    displayWord= displayWord.split('/')
    index=-1
    for char in secretWord:
        index+=1
        if char in lettersGuessed:
            displayWord[index]=char
    return ' '.join(displayWord)
            
            


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    
    lettersRemaining=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for char in lettersGuessed:
    ##in case user guesses same letter twice
        if char in lettersRemaining:
            lettersRemaining.remove(char)
    stringLetters=''.join(lettersRemaining)
    return stringLetters
            
    

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
    # FILL IN YOUR CODE HERE...
    ##introductory text
    print 'Welcome to the game, Hangman!'
    print 'I am thinking of a word that is '+str(len(secretWord))+' letters long.'
    print '-----------'
    ##getting started
    triesRemaining=8
    lettersGuessed=[]
    while triesRemaining>0:
        lettersRemaining=getAvailableLetters(lettersGuessed)
        print 'You have '+ str(triesRemaining)+ ' guesses left.'
        print 'Available letters: '+ str(getAvailableLetters(lettersGuessed))
        guess=raw_input('Please guess a letter:')
        guessLowerCase=guess.lower()
        if guessLowerCase in lettersGuessed:
            print 'Oops! You\'ve already guessed that letter: ' + str (getGuessedWord(secretWord, lettersGuessed))
            print '-----------'
        elif guessLowerCase in lettersRemaining:
            if guessLowerCase in secretWord:
                lettersGuessed+=[guessLowerCase]
                print 'Good guess: ' +str(getGuessedWord(secretWord, lettersGuessed))
                print '-----------'
            else:
                lettersGuessed+=[guessLowerCase]
                triesRemaining -=1
                print 'Oops! That letter is not in my word: ' +str(getGuessedWord(secretWord, lettersGuessed))
                print '-----------'
        else:
            print 'I don\'t recognize that character. Please try again!'
            print '-----------'
        if isWordGuessed (secretWord, lettersGuessed) == True:
            print 'Congratulations, you won!'
            break
    if triesRemaining==0:
        print 'Sorry, you ran out of guesses. The word was '+ str(secretWord)






# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
