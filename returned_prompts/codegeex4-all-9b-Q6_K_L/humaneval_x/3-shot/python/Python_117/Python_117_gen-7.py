    vowels = "aeiouAEIOU"
    result = []
    for word in s.split():
        if len(word) == n:
            count = sum(1 for c in word if c not in vowels)
            if count == n:
                result.append(word)
    return result

