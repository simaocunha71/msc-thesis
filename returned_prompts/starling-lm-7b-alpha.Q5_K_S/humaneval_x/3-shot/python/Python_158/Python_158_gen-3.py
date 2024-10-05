    def is_unique(word):
        return len(set(word)) == len(word)

    def lexicographically_first(word1, word2):
        if word1 < word2:
            return word1
        return word2

    max_word = ""
    max_num_unique_chars = 0

    for word in words:
        if is_unique(word) and len(word) > max_num_unique_chars:
            max_num_unique_chars = len(word)
            max_word = word
        elif len(word) == max_num_unique_chars and word < max_word:
            max_word = word

    return max_word


