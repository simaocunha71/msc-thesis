    def count_consonants(word):
        return sum(1 for c in word if c.lower() in 'bcdfghjklmnpqrstvwxyz')

    return [word for word in s.split() if count_consonants(word) == n]


