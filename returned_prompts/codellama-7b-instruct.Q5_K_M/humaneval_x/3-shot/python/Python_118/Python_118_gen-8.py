    for i in range(len(word)-1, 0, -1):
        if word[i].isalpha() and word[i].islower() and (word[i].isalpha() and word[i-1].isupper()):
            return word[i]
        
    return ""