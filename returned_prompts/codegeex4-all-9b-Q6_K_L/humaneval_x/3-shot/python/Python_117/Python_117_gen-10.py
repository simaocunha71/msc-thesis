    def count_consonants(word):
        count = 0
        for c in word:
            if c.lower() in "bcdfghjklmnpqrstvwxyz":
                count += 1
        return count

    result = []
    words = s.split()
    for word in words:
        if count_consonants(word) == n:
            result.append(word)

    return result

