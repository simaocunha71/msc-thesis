    def is_consonant(letter):
        return letter not in 'aeiou '

    def count_consonants(word):
        count = 0
        for letter in word:
            if is_consonant(letter):
                count += 1
        return count

    result = []
    for word in s.split():
        if count_consonants(word) == n:
            result.append(word)

    return result


