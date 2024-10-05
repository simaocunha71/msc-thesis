    vowels = ["A", "E", "I", "O", "U"]
    consonants = ["B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z"]
    result = ""
    for i in range(len(word)-1):
        if word[i] in consonants and word[i+1] in consonants:
            continue
        elif word[i] in consonants and word[i+1] in vowels:
            return word[i+1]
        elif word[i] in vowels and word[i+1] in consonants:
            return word[i]
    return result


