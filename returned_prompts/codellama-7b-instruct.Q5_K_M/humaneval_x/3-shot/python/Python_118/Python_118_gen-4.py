    for i in range(len(word)-1, -1, -1):
        if word[i].isalpha() and (word[i].islower() and word[i] not in "aeiou" or word[i].isupper() and word[i] not in "AEIOU"):
            for j in range(i-1, -1, -1):
                if word[j].isalpha() and (word[j].islower() and word[j] not in "aeiou" or word[j].isupper() and word[j] not in "AEIOU"):
                    if word[i].lower() != word[j].lower():
                        return word[i]
    return ""


