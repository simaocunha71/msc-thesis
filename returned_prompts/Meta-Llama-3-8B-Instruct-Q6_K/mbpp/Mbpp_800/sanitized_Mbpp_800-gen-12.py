import string
def remove_all_spaces(s):
    s = s.lower()
    s = s.translate(str.maketrans('', '', string.punctuation))
    return s.replace(" ", "")