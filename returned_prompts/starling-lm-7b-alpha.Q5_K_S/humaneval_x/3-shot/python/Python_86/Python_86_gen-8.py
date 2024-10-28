    def anti_shuffle(s):
        result = []
        for word in s.split():
            result.append(''.join(sorted(word)))
        return ' '.join(result)


