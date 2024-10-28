    result = []
    words = s.split()
    for word in words:
        vowels = ['a', 'e', 'i', 'o', 'u']
        if len([c for c in word if c not in vowels]) == n:
            result.append(word)
    return result


