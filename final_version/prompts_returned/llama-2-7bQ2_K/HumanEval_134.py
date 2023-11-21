
def check_if_last_char_is_a_letter(txt):
    '''
    Create a function that returns True if the last character
    of a given string is an alphabetical character and is not
    a part of a word, and False otherwise.
    Note: "word" is a group of characters separated by space.

    Examples:
    check_if_last_char_is_a_letter("apple pie") ➞ False
    check_if_last_char_is_a_letter("apple pi e") ➞ True
    check_if_last_char_is_a_letter("apple pi e ") ➞ False
    check_if_last_char_is_a_letter("") ➞ False 
    '''

    def f(txt):
        if txt == '': # empty input, just return False
            return False 
        
        last = txt.rfind(' ') # find last space in string
        return txt[last:].isalpha() and not any(w.isalpha() for w in txt[:-1]) #check if the last character is a letter and it's not part of word and it will always be True 
        
    return f
