    def is_unique(s):
        return len(s) == len(set(s))

    max_unique = ""
    max_count = 0
    for word in words:
        if is_unique(word):
            if len(word) > max_count:
                max_count = len(word)
                max_unique = word
            elif len(word) == max_count:
                if word < max_unique:
                    max_unique = word

    return max_unique


