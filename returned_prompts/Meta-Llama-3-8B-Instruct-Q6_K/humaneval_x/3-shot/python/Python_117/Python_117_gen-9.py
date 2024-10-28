    def is_consonant(char):
        vowels = 'aeiouAEIOU'
        return char not in vowels

    result = []
    n_consonants = 0
    word = ''
    for char in s:
        if char == ' ':
            if n_consonants == n:
                result.append(word)
            word = ''
            n_consonants = 0
        else:
            if is_consonant(char):
                n_consonants += 1
            word += char
    if n_consonants == n:
        result.append(word)

    return result
