    def find_max(words):
        def count_unique(word):
            return len(set(word))

        max_count = 0
        max_word = ''
        for word in words:
            if count_unique(word) > max_count:
                max_word = word
                max_count = count_unique(word)
        return max_word


