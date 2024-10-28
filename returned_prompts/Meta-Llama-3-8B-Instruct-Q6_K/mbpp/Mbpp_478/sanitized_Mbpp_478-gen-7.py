import string
def remove_lowercase(s):
    return s.upper().translate(str.maketrans('', '', string.ascii_lowercase))