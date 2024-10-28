    def max_num_unique_chars(word):
        return len(set(word))

    words.sort(key=max_num_unique_chars)
    return words[-1]


