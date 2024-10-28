    def count_unique_characters(word):
        return len(set(word))

    max_unique_characters = 0
    max_word = ""

    for word in words:
        unique_characters = count_unique_characters(word)

        if unique_characters > max_unique_characters:
            max_unique_characters = unique_characters
            max_word = word
        elif unique_characters == max_unique_characters:
            if word < max_word:
                max_word = word

    return max_word

