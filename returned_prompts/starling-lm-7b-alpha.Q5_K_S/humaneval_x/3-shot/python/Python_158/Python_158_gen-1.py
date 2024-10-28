    def is_unique(word):
        char_set = set()
        for char in word:
            char_set.add(char)
        if len(char_set) == len(word):
            return True
        return False

    max_word = ''
    max_count = 0
    for word in words:
        if is_unique(word) and len(word) > max_count:
            max_count = len(word)
            max_word = word

    return max_word


