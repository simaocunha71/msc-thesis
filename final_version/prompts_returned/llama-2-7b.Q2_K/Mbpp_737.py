"""
Write a function to check whether the given string is starting with a vowel or not using regex.
assert check_str("annie")
"""

def is_vowel(s):
    """Write a method that checks if the string starts with one of the vowels: [a,e,i,o]"""
    return re.match('[aeio]', s) != None
