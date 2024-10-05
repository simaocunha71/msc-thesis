    vowels = ["a", "e", "i", "o", "u"]
    def is_consonant(char):
        return char not in vowels

    def is_word(word):
        return len(word) != 0 and word[0] != " "

    def count_consonants(word):
        count = 0
        for char in word:
            if is_consonant(char):
                count += 1
        return count

    result = []
    for word in s.split():
        if is_word(word):
            if count_consonants(word) == n:
                result.append(word)

    return result


