    def find_max(words):
        def unique_chars(word):
            return len(set(word))
        return max(words, key=unique_chars)


