
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
    result = ''
    for letter in message:
        if letter.islower():
            result += letter.upper()
        else:
            result += letter.lower()
    for letter in result:
        if letter in 'aeiou':
            result = result.replace(letter, result[result.index(letter) + 2])
    return result

