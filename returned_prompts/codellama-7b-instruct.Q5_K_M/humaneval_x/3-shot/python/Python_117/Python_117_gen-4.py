    result = []
    word_list = s.split()
    for word in word_list:
        vowels = "aeiou"
        if len(word) == n and word.count(vowels) != len(word):
            result.append(word)

    return result
