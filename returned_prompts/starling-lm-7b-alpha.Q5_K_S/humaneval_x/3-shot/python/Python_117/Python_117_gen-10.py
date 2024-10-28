    def consonant(c):
        return not (c in 'aeiou ')

    def count_consonants(word):
        return sum(consonant(c) for c in word)

    result = []
    for word in s.split():
        if count_consonants(word) == n:
            result.append(word)

    return result


