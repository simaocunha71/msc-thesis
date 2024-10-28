    def is_consonant(char: str) -> bool:
        return char.lower() not in 'aeiou'

    words = s.split()
    result = []

    for word in words:
        consonants = sum(1 for char in word if is_consonant(char))
        if consonants == n:
            result.append(word)

    return result


