
def select_words(s, n):
    words = s.split()
    return [word for word in words if word.lower().count('a') + word.lower().count('e') + word.lower().count('i') + word.lower().count('o') + word.lower().count('u') == n]
