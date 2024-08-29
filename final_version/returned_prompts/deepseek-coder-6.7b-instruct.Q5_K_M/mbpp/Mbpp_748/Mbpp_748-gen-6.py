"""
def capital_words_spaces(text):
    # First, we split the text into words using the split() function.
    words = text.split()
    # Then, we join the words back together with a space in between them.
    # We use a list comprehension to check if the word starts with a capital letter,
    # and if it does, we add a space before it.
    return ' '.join(word if word[0].islower() else ' ' + word for word in words)
"""

