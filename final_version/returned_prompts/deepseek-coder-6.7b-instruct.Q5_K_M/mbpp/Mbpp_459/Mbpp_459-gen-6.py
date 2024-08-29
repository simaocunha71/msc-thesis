
def remove_uppercase(s):
    output = ""
    for word in s.split(" "):
        if not word.isupper():
            output += word + " "
    return output.strip()

print(remove_uppercase('cAstyoUrFavoRitETVshoWs'))


# Alternatively, using List Comprehension:

def remove_uppercase(s):
    return ' '.join(word for word in s.split() if not word.isupper())

print(remove_uppercase('cAstyoUrFavoRitETVshoWs'))


# Alternatively, using regular expressions:

import re

def remove_uppercase(s):
    return re.sub(r'(?<=[a-z])(?=[A-Z])', ' ', s)

print(remove_uppercase('cAstyoUrFavoRitETVshoWs'))


# Alternatively, using a loop and conditional:

def remove_uppercase(s):
    result = ''
    for c in s:
        if c.isupper():
            result += ' '
        result += c
    return ''.join(w for w in result.split() if not w.isupper())

print(remove_uppercase('cAstyoUrFavoRitETVshoWs'))


# Alternatively, using a loop and conditional:

def remove_uppercase(s):
    return ''.join(c if c.islower() else ' ', s).strip()

print(remove_uppercase('cAstyoUrFavoRitETVshoWs'))


# Alternatively, using a loop and conditional:

def remove_uppercase(s):
    return ''.join(c if c.islower() else '', s)

print(remove_uppercase('cAstyoUrFavoRitETVshoWs'))

"""
Explanation: 

The function takes a string as input, splits it into words, checks if each word is uppercase, and if it is not, adds it to the output string. The function returns the output