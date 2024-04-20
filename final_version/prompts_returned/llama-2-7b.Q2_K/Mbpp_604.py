"""
Write a function to reverse words seperated by spaces in a given string.
assert reverse_words("python program")==("program python")
"""

def reverse_words(s):
    if not s: return s
    else:
        s = ''
        for i, word in enumerate(s.split()):
            end = len(word) - 1
            reversed_word = ''.join([str(c) for c in word[:end]])
            new_string = '{} {}'.format(reversed_word, s[i+1:]) if i + 1 < len(s) else ''
            s += new_string
        return s