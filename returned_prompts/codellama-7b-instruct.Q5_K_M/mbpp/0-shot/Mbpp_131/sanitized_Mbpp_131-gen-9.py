def reverse_vowels(s):
    vowels = "aeiouAEIOU"
    rv = ""
    for c in s:
        if c in vowels:
            rv = c + rv
        else:
            rv = rv + c
    return rv