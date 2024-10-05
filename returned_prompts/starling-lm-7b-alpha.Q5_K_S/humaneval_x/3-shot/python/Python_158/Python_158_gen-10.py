    def count_unique_characters(word):
        return len(set(word))

    max_count = 0
    max_word = ""
    for word in words:
        count = count_unique_characters(word)
        if count > max_count:
            max_count = count
            max_word = word
        elif count == max_count:
            if word < max_word:
                max_word = word
    return max_word


