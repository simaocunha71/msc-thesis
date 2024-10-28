    def count_unique_chars(word):
        return len(set(word))

    max_unique_count = 0
    max_unique_word = ""

    for word in words:
        unique_count = count_unique_chars(word)
        if unique_count > max_unique_count:
            max_unique_count = unique_count
            max_unique_word = word
        elif unique_count == max_unique_count:
            if word < max_unique_word:
                max_unique_word = word

    return max_unique_word