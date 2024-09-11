"""
def reverse_vowels(s):
    s = list(s)
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i in range(len(s)):
        if s[i].lower() in vowels:
            j = len(s) - i - 1
            while j > i:
                if s[j].lower() in vowels:
                    s[j], s[i] = s[i], s[j]
                    j -= 1
                    break
                j -= 1
    return ''.join(s)
"""

