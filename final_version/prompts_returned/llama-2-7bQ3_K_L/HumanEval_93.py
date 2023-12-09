
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

    for letter in message:
        if letter.islower():
            replace_letter = ord(message[letter + 1]) - len("a")
            encoded_letter = chr((ord(letter) - 32) + replace_letter)
            
        elif letter.isupper():
            replace_letter = ord('z') - (len('a') + 1)
            encoded_letter = chr((ord(letter) - 97) + replace_letter)
        else:
            encoded_letter = letter
        
    return ''.join(encoded_letter for letter in message)

def decode(message):
    """
    Write a function that takes a message, and decodes it into its original
    form. Assume only letters (no numbers or other characters). 
    
    Examples:
    >>> decode('TGST')
    'test'
    >>> decode('tHKS KS C MGSSCGG')
    'This is a message'
    """

    for letter in message:
        if letter.islower():
            replace_letter = ord(message[letters.get(letter) + 1]) - len("a")
            encoded_letter = chr((ord(letter) - ord('a') - 32) - replace_letter)
            
        elif letter.isupper():
            replace_letter = ord('y') - (len('z') + 1)
            encoded_letter = chr((ord(letter) - ord('Z') - 97) - replace_letter)
        else:
            encoded_letter = letter        

    return ''.join(encoded_letter for letter in