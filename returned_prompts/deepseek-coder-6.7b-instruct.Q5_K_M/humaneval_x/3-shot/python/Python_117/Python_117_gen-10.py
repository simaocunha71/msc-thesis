    def count_consonants(word):
        return sum(1 for char in word if char.lower() in 'bcdfghjklmnpqrstvwxyz')

    return [word for word in s.split() if count_consonants(word) == n]


