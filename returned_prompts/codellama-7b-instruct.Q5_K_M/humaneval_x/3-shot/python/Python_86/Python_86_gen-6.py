    def shuffle_word(word):
        return ''.join(sorted(word))

    return ' '.join(map(shuffle_word, s.split()))


