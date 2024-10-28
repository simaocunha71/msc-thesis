    def is_consonant(c):
        return c not in 'aeiou'

    result = []
    i = 0
    while i < len(s):
        j = i
        while j < len(s) and s[j] != ' ':
            j += 1
        if j - i >= n and all(is_consonant(c) for c in s[i:j]):
            result.append(s[i:j])
        i = j + 1

    return result


