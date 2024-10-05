    words = s.split()
    new_words = []
    for word in words:
        char_list = sorted(word)
        new_word = ''.join(char_list)
        new_words.append(new_word)
    return ' '.join(new_words)  # return the joined string


