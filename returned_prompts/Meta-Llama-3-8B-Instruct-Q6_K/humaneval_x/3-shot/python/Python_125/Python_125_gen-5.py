    words = txt.split()
    if len(words) > 0 and len(words[0]) > 0 and words[0][0].isalpha():
        return words
    else:
        return [len([c for c in txt if c.islower() and (ord(c) - ord('a')) % 2 == 1])]  # count the number of lower-case letters with odd order in the alphabet


