
def count_letters(s):
    return {letter: s.count(letter) for letter in set(s)}


