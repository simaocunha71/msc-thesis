    vowels = "aeiouAEIOU"
    result = ""

    for i in range(len(word) - 2, -1, -1):
        if word[i] in vowels and word[i + 1] not in vowels and word[i + 2] not in vowels:
            result = word[i]
            break

    return result

