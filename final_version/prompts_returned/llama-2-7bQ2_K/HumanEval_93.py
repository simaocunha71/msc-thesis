
def encode(message):
    """
    Write a function that takes a message, and encodes in such a 
    way that it swaps case of all letters, replaces all vowels in 
    the message with the letter that appears 2 places ahead of that 
    vowel in the english alphabet. 
    Assume only letters. 
    
    Examples:
    >>> encode('test')
    'TGST'
    >>> encode('This is a message')
    'tHKS KS C MGSSCGG'
    """

    new_message = ''
    for letter in message.lower():  
        if letter == "a" and (letter - 3) == "e":      # Replace e with i, etc
            new_message += 'i'
        elif letter == "a" and (letter - 10) == "t":     # Replace t with d, etc
            new_message += 'd'
        else:
            if letter == 'e':                                # Replace e with i or o, etc
                if (letter - 6) == 'i':                    # OR
                elif (letter - 5) == 'o':
                    new_message += 'o'
            elif letter == 'h':                             # Replace h with a or b, etc
                if len(word.lower()) % 2 != 0:              # OR
                    pass
                else:
                    new_message += 'a'
        print(letter + " in position" + str(position) + ': ' , "is " + letter)     # Print letter to help you understand the code! :)
        if (not letter == 'h'):  
            print("in position", position + 1, ": ", "is ")
        new_message += letter
        
    return new_message                              ## Return a new version of message.lower() with swapped letters, etc.

def decode(encoded_message):
    """
    Write a function that takes the encoded message and decodes it 
    so that each letter is changed to lowercase and vowels are replaced by their English alphabet order counterparts.
    
    >>> encode('test')
    'TGST'
    >>>