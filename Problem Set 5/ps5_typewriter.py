def insertNewlines(text, lineLength):
    """
    Given text and a desired line length, wrap the text as a typewriter would.
    Insert a newline character ("\n") after each word that reaches or exceeds
    the desired line length.

    text: a string containing the text to wrap.
    line_length: the number of characters to include on a line before wrapping
        the next word.
    returns: a string, with newline characters inserted appropriately. 
    """
##    if text[lineLength - 1] == ' ':
##        text = text[:lineLength-1]+'\n' + text[lineLength:]
##    ##distance between last line-break and lineLength:
##
##    ##find the first space on or before last linebreak and replace it with a space
##        
##    (text[text.rfind('\n'):(text.rfind('\n')+lineLength]).find(' ') == 
##    ##find the next space and replace with \n: text[lineLength:].find[' '] (finds the index)
##    else:
##        text = text[:(text[lineLength:].find[' ']-1)]+'\n'+text [(text[lineLength:].find[' ']+1):]
##    return insertNewlines(text, lineLength+lineLength)
    ##base case: if distance between last line break and end of sentence is less than or equal to line break:
    n = text.rfind('\n')
    if (n<1):
        s = text[(lineLength-1):].find(' ')
    elif n >= (len(text)-lineLength):
        return text
    else:
        if (n<0):
            n = 0;
        s = text[(n+(length-1)):].find(' ')
    print s
    print '\n'
    text = text[:s] + '\n' + text[(s+1):]
    print text
    return insertNewlines(text, lineLength)


##  text = text[text[text.rfind('\n'):(text.rfind('\n')+lineLength)].find(' ')- 1] +'\n' + text[text[text.rfind('\n'):(text.rfind('\n')+lineLength)].find(' ')+ 1]
##    print text   
 ##   return insertNewlines(text, lineLength)
                                                                                            
