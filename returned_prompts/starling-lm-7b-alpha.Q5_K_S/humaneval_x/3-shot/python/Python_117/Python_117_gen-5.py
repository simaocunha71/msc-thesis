    vowels = "AEIOUaeiou"
    consonants = "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz"
    res = []
    for word in s.split():
        cnt = 0
        for letter in word:
            if letter in consonants:
                cnt += 1
        if cnt == n:
            res.append(word)
    return res


