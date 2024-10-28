def capital_words_spaces(s):
    # Split into words
    words = s.split()
    # Add spaces
    words = [word[0] + ' ' + word[1:] for word in words]
    # Join back
    return ' '.join(words)

