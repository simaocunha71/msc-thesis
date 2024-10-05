    consonants = 'BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz'
    vowels = 'AEIOUaeiou'

    def is_consonant(c):
        return c in consonants

    def is_vowel(c):
        return c in vowels

    def count_consonants(word):
        count = 0
        for char in word:
            if is_consonant(char):
                count += 1
        return count

    words = s.split()
    result = []
    for word in words:
        if count_consonants(word) == n:
            result.append(word)
    return result


