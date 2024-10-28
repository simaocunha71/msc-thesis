    def anti_shuffle_helper(word):
        return ''.join(sorted(word))

    return ' '.join(map(anti_shuffle_helper, s.split()))

