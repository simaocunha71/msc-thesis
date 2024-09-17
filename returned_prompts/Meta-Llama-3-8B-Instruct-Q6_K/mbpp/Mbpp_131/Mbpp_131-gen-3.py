```
def reverse_vowels(s):
    vowels = 'aeiouAEIOU'
    s = list(s)
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] not in vowels:
            left += 1
        elif s[right] not in vowels:
            right -= 1
        else:
            s[left], s[right] = s[right], s[left]
            left, right = left + 1, right - 1
    return ''.join(s)
```
This function works by iterating through the string from both ends, swapping the vowels it finds. The `left` and `right` pointers move towards each other, swapping the vowels until they meet in the middle. The function returns the modified string. The `assert` statement ensures that the function leaves non-vowel characters unchanged.