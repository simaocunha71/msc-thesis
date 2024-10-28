    vowels = "AEIOUaeiou"
    word = word[::-1]  # reverse the word
    result = ""
    for char in word:
        if char in vowels:
            result = char
            break
        if char not in vowels:
            word = word[:-1]
            if not word or word[-1] in vowels:
                break
    return result[::-1]  # reverse the result back to original order


