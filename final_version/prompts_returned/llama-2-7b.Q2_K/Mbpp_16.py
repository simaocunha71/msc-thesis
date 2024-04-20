"""
Write a function to that returns true if the input string contains sequences of lowercase letters joined with an underscore and false otherwise.
assert text_lowercase_underscore("aab_cbbbc")==(True)
"""
import re

def text_lowercase_underscore(text):
    def _add_uppercase_letter(s1, s2):
        u = ''
        for c in list(s1):
            if c.isalnum():
                u += c
            else:
                u += "{" + str(int((ord(c) + 97) % 256)) + ", "
                u += c
        return u[:-2]

    pattern = re.compile("[a-z]{2,}_?")
    def add_lowercase_letter(s1, s2):
        if not (s1 or s2).startswith('"'):
            return '"' + _add_uppercase_letter(s1, s2) + '"'
        else:
            return "%s-%s" % (_add_uppercase_letter(s1, '""'), _add_uppercase_letter("""", s2)) if s1 or s2.startswith('"') else _add_uppercase_letter('"', '"'" + s1 + "'")
    return pattern.fullmatch(text) or True
\end{code}