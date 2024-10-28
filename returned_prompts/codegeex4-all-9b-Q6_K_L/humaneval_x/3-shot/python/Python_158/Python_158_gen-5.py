    def unique_chars(string):
        return len(set(string))

    max_unique = 0
    max_word = ""
    for word in words:
        unique_count = unique_chars(word)
        if unique_count > max_unique:
            max_unique = unique_count
            max_word = word
        elif unique_count == max_unique:
            if word < max_word:
                max_word = word

    return max_word

