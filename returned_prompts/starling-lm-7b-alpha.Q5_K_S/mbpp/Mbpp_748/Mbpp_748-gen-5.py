def capital_words_spaces(string):
    if len(string) <= 1:
        return string
    else:
        if string[0].isupper():
            return string[0] + ' ' + capital_words_spaces(string[1:])
        else:
            return string[0] + capital_words_spaces(string[1:])




"""
def capital_words_spaces(s):
    if len(s) <= 1:
        return s
    else:
        if s[0].isupper():
            return s[0] + ' ' + capital_words_spaces(s[1:])
        else:
            return s[0] + capital_words_spaces(s[1:])
"""


"""
def capital_words_spaces(s):
    if len(s) <= 1:
        return s
    else:
        if s[0].isupper():
            return s[0] + ' ' + capital_words_spaces(s[1:])
        else:
            return s[0] + capital_words_spaces(s[1:])
"""

# assert capital_words_spaces("Python") == 'Python'
# assert capital_words_spaces("Hello World") == 'Hello World'

"""
def capital_words_spaces(s):
    if len(s) <= 1:
        return s
    else:
        if s[0].isupper():
            return s[0] + ' ' + capital_words_spaces(s[1:])
        else:
            return s[0] + capital_words_spaces(s[1:])
"""


# assert capital_words_spaces("Python") == 'Python'
# assert capital_words_spaces("Hello World") == 'Hello World'

"""
def capital_words_spaces(s):
    if len(s) <= 1:
        return s
    else:
        if s[0].isupper():
            return s[0] + ' ' + capital_words_spaces(s[1:])
        else:
