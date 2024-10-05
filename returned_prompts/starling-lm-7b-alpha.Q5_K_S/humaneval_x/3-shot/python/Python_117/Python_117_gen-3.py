    def is_consonant(c):
        return c != 'a' and c != 'e' and c != 'i' and c != 'o' and c != 'u'

    def count_consonants(word):
        count = 0
        for c in word:
            if is_consonant(c):
                count += 1
        return count

    words = s.split()
    result = []
    for word in words:
        if count_consonants(word) == n:
            result.append(word)
    return result


