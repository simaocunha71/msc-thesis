    def is_unique(word):
        letters = set(word)
        if len(word) == len(letters):
            return True
        return False

    def is_greater(word1, word2):
        if len(word1) == len(word2):
            return word1 < word2
        else:
            return len(word1) > len(word2)

    result = ""
    max_length = 0
    for word in words:
        if is_unique(word):
            if len(word) > max_length:
                result = word
                max_length = len(word)
            elif len(word) == max_length and is_greater(result, word):
                result = word

    return result


