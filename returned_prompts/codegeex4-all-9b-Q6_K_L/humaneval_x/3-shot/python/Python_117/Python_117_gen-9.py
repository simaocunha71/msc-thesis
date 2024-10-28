    vowels = set("aeiouAEIOU")
    result = []
    for word in s.split():
        count = sum(1 for c in word if c.lower() not in vowels)
        if count == n:
            result.append(word)
    return result

