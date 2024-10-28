    def find_max(words):
        max_length = 0
        max_word = ''

        for word in words:
            if len(set(word)) > max_length:
                max_length = len(set(word))
                max_word = word
            elif len(set(word)) == max_length:
                max_word = min(max_word, word)

        return max_word


