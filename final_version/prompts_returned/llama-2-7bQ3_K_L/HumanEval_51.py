

def remove_vowels(text):
    """
    remove_vowels is a function that takes string and returns string without vowels.
    >>> remove_vowels('')
    ''
    >>> remove_vowels("abcdef\nghijklm")
    'bcdf\nghjklm'
    >>> remove_vowels('abcdef')
    'bcdf'
    >>> remove_vowels('aaaaa')
    ''
    >>> remove_vowels('aaBAA')
    'B'
    >>> remove_vowels('zbcd')
    'zbcd'
    """

    def remove_vowel(word):
        word = list(map(str, word))
        vowel_list = ['aeiou', 'AEIOU']
        
        for letter in word:
            if letter.lower() in vowel_list:
                return ''
            
        return ' '.join(word)
    return remove_vowel
