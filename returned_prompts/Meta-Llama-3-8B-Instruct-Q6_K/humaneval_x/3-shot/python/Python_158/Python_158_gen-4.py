    def find_max(words):
        max_word = max(words, key=lambda x: (len(set(x)), x))
        return max_word


