    for i in range(len(word) - 1, -1, -1):
        if word[i] in 'aeiouAEIOU':
            if i < len(word) - 1 and word[i+1] not in 'aeiouAEIOU':
                return word[i]
    return ''


