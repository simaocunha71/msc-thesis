def reverse_vowels(s):
    vowels = 'aeiou'
    ans = ''
    for c in s:
        if c in vowels:
            ans = c + ans
        else:
            ans += c
    return ans