    def count_uniques(word):
        return len(set(word))

    def is_unique(word):
        return count_uniques(word) == len(word)

    return max(words, key=lambda word: (count_uniques(word), -len(word)))


