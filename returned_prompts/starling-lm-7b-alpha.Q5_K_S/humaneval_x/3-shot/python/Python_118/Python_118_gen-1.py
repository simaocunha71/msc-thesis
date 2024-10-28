    vowels = "aeiou"
    for idx, c in enumerate(word):
        if c not in vowels:
            left = idx - 1
            right = idx + 1
            if left >= 0 and word[left] in vowels:
                return word[left]
            elif right < len(word) and word[right] in vowels:
                return word[right]

    return ""


