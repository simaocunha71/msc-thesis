

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
    
    # Vowel is a letter in alphabet. In English "a" and "e" are called vowels,
    # if we are going to remove "e", then it will be counted as consonant.
    # So here we check whether the first character of string is alphabetical or not. If yes, then we remove vowel from string.
    
    new_str = ''
    for i in range(len(text)):
        ch=text[i]
        if ch.isalpha():
            print("The character at " + str(i) + " is a letter")
            new_str+=ch
        else:
            print("The character at " + str(i) + " is not a letter, we will use it ")
            new_str+=" "
    return new_str

if __name__ == "__main__":
    
    text = remove_vowels('aaBAA')
    print("\n\nRemove vowel from string \n\taaBAA → aB   \n\tttt → tt \n\tb → b')
