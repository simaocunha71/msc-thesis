    vowels = 'aeiouAEIOU'
    for i in range(len(word) - 2, -1, -1):
        if word[i] in vowels:
            if word[i-1].lower() not in 'aeiou' and word[i+1].lower() not in 'aeiou':
                return word[i]
    return ""


