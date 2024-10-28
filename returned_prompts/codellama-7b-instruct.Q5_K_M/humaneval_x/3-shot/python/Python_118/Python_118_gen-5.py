    for i in range(1, len(word)):
        if word[i-1].isalpha() and word[i].isalpha():
            if not word[i-1].isupper() and word[i].isupper():
                return word[i]
            elif not word[i].isupper() and word[i-1].isupper():
                return word[i-1]
            elif word[i-1].islower() and word[i].islower():
                return word[i]
            elif word[i-1].islower() and word[i].islower():
                return word[i-1]
    return ""


