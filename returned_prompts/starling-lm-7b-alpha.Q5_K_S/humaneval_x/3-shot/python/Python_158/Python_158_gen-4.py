    def unique(word):
        return len(set(word))

    def compare(word1, word2):
        if unique(word1) == unique(word2):
            return word1 < word2
        return unique(word1) > unique(word2)

    return max(words, key=lambda word: (unique(word), word), default='')


