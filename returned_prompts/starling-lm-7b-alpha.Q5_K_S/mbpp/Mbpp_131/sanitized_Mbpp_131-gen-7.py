def reverse_vowels(s):
    vowel = "aeiou"
    s = list(s)
    i,j = 0,len(s)-1
    while i < j:
        if s[i] in vowel:
            s[i],s[j] = s[j],s[i]
            j -= 1
        else:
            i += 1
    return "".join(s)