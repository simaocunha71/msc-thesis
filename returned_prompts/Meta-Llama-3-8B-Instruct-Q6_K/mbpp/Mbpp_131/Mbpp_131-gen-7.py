```
def reverse_vowels(s):
    vowels = 'aeiouAEIOU'
    s_list = list(s)
    left, right = 0, len(s) - 1
    while left < right:
        if s_list[left] not in vowels:
            left += 1
        elif s_list[right] not in vowels:
            right -= 1
        else:
            s_list[left], s_list[right] = s_list[right], s_list[left]
            left, right = left + 1, right - 1
    return ''.join(s_list)
```
The function takes a string `s` as input and returns the string with vowels reversed. It uses a two-pointer approach, initializing `left` and `right` pointers at the start and end of the string respectively. It then iterates through the string, swapping the vowels at the `left` and `right` pointers when they are found. The function returns the modified string.

The unit test `assert reverse_vowels("Python") == "Python"` ensures that the function does not reverse the string when no vowels are present, which is the expected behavior. This test also confirms that the function correctly handles strings with only one vowel. 





Note: The problem statement does not explicitly mention that 'y' is not a vowel, but this is implied by the unit test `assert reverse_vowels("Python") == "Python"`, which suggests that 'y' should not be considered a vowel. 