def extract_values(s):
    '''
    >>> extract_values('"Python", "PHP", "Java"')
    ['Python', 'PHP', 'Java']
    '''
    return [i[1:-1] for i in s.split('", "')]


# Created by: haya17
# Date: 27/11/2018

def extract_values(s):
    # split the string by double quotes
    parts = s.split('"')
    # get a list of values
    values = [part[1:-1] for part in parts if part.startswith('"')]
    return values


# Created by: haya17
# Date: 27/11/2018


"""
Write a function to check if a given string is a palindrome.

assert is_palindrome('racecar') == True
assert is_palindrome('hello') == False
"""

def is_palindrome(s):
    '''
    >>> is_palindrome('racecar')
    True
    >>> is_palindrome('hello')
    False
    '''
    # return True if the string is equal to its reverse
    return s == s[::-1]


# Created by: haya17
# Date: 27/11/2018


"""
Write a function to return a string with all vowels removed.

assert remove_vowels('hello') == 'hll'
assert remove_vowels('Python') == 'Pythn'
"""

def remove_vowels(s):
    '''
    >>> remove_vowels('hello')
    'hll'
    >>> remove_vowels('Python')
    'Pythn'
    '''
    # create a set of vowels
    vowels = set('aeiouAEIOU')
    # return the string with vowels removed
    return ''.join([c for c in s if c not in vowels])


# Created by: haya17
# Date: 27/11/