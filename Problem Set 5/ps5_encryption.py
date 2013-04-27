# 6.00x Problem Set 5
#
# Part 1 - HAIL CAESAR!

import string
import random

WORDLIST_FILENAME = "words.txt"

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    inFile = open(WORDLIST_FILENAME, 'r')
    wordList = inFile.read().split()
    print "  ", len(wordList), "words loaded."
    return wordList

def isWord(wordList, word):
    """
    Determines if word is a valid word.

    wordList: list of words in the dictionary.
    word: a possible word.
    returns True if word is in wordList.

    Example:
    >>> isWord(wordList, 'bat') returns
    True
    >>> isWord(wordList, 'asdf') returns
    False
    """
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\\:;'<>?,./\"")
    return word in wordList

def randomWord(wordList):
    """
    Returns a random word.

    wordList: list of words  
    returns: a word from wordList at random
    """
    return random.choice(wordList)

def randomString(wordList, n):
    """
    Returns a string containing n random words from wordList

    wordList: list of words
    returns: a string of random words separated by spaces.
    """
    return " ".join([randomWord(wordList) for _ in range(n)])

def randomScrambled(wordList, n):
    """
    Generates a test string by generating an n-word random string
    and encrypting it with a sequence of random shifts.

    wordList: list of words
    n: number of random words to generate and scamble
    returns: a scrambled string of n random words

    NOTE:
    This function will ONLY work once you have completed your
    implementation of applyShifts!
    """
    s = randomString(wordList, n) + " "
    shifts = [(i, random.randint(0, 25)) for i in range(len(s)) if s[i-1] == ' ']
    return applyShifts(s, shifts)[:-1]

def getStoryString():
    """
    Returns a story in encrypted text.
    """
    return open("story.txt", "r").read()


# (end of helper codeProblem 1: Encryption
#
def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    ## alphabet to dictionary: keys = letters, values = position in alphabet
    shift=26-shift
    import string
    lowerAlpha = string.ascii_lowercase
    lowerAlphaDict = {}
    for char in lowerAlpha:
        val=lowerAlpha.index(char)
        lowerAlphaDict[char]=val
    upperAlpha = string.ascii_uppercase
    upperAlphaDict = {}
    for char in upperAlpha:
        val = upperAlpha.index(char)
        upperAlphaDict[char]=val    
    ## shift each value in dictionary
    for char in lowerAlphaDict:
        lowerAlphaDict[char] -=shift
    for char in upperAlphaDict:
        upperAlphaDict[char]-=shift
    ## change dictionary so that key = original letter, value = new letter
    caesarShift={}
    for char in lowerAlphaDict:
        caesarShift[char]= lowerAlpha[lowerAlphaDict[char]]
    for char in upperAlphaDict:
        caesarShift[char] = upperAlpha[upperAlphaDict[char]]
    return caesarShift

        

def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    textList=[]
    textList+=text
    caesarList=[]
     
    for char in textList:
        ##switches alpha characters to code
        if char in coder:
            caesarList+=coder[char]
        ##leaves non-alpha characters alone
        else:
            caesarList+=char
    caesar=''.join(caesarList)
    return caesar
    

def applyShift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. Lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.

    text: string to apply the shift to
    shift: amount to shift the text (0 <= int < 26)
    returns: text after being shifted by specified amount.
    """
    return applyCoder(text, buildCoder(shift))
   
    
#
# Problem 2: Decryption
#
def findBestShift(wordList, text):
    """
    Finds a shift key that can decrypt the encoded text.

    text: string
    returns: 0 <= int < 26
    """
    import string
        ##set best case number of real words
    mostWords=0
    ##set best case shift: shift for which text has highest number of real words
    bestShift = 0
    ## while shift is <= 26
    shift = 0
    for shift in range (0,26):
        ## perform shift
        ## CALCULATING THE NUMBER OF REAL WORDS
        ## for each element of shifted textList:
        ##split text into list of strings
        shiftMsg = applyShift (text, shift)
        shiftList=shiftMsg.split (' ')
        count=0
        for element in shiftList:           
            ## if element in wordList:
            if isWord(wordList, element):
                ## count+=1
                count+=1
        ## COMPARING CURRENT SHIFT TO BEST SHIFT
        ## if number is better than the current best case replace best case with current case
        if count > mostWords:
            mostWords=count
            bestShift=shift
        ## Add 1 to the shift and loop again
        shift+=1
    ##return best case shift
    return bestShift

def decryptStory():
    """
    Using the methods you created in this problem set,
    decrypt the story given by the function getStoryString().
    Use the functions getStoryString and loadWords to get the
    raw data you need.

    returns: string - story in plain text
    """
    ## Decrypted story:
    ## 'Jack Florey is a mythical character created on the spur of a moment to help cover an insufficiently planned hack. He has been registered for classes at MIT twice before, but has reportedly never passed a class. It has been the tradition of the residents of East Campus to become Jack Florey for a few nights each year to educate incoming students in the ways, means, and ethics of hacking.\n'
    wordList = loadWords()
    text = getStoryString()
    return applyShift(text, findBestShift(wordList,text))
    
   

#
# Build data structures used for entire session and run encryption
#

if __name__ == '__main__':
    # To test findBestShift:
    wordList = loadWords()
    s = applyShift('Hello, world!', 8)
    bestShift = findBestShift(wordList, s)
    assert applyShift(s, bestShift) == 'Hello, world!'
    # To test decryptStory, comment the above four lines and uncomment this line:
    #    decryptStory()
