def reverse_vowels(s):
    s = list(s)
    i, j = 0, len(s) - 1
    while i < j:
        if s[i].lower() not in 'aeiou':
            i += 1
        elif s[j].lower() not in 'aeiou':
            j -= 1
        else:
            s[i], s[j] = s[j], s[i]
            i, j = i + 1, j - 1
    return ''.join(s)