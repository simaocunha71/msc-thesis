    def count_consonants(word):
        return sum(1 for c in word if c.lower() in "bcdfghjklmnpqrstvwxyz")

    words = s.split()
    return [word for word in words if count_consonants(word) == n]


