```
def reverse_vowels(s):
    vowels = "aeiou"
    s = list(s)
    left = 0
    right = len(s) - 1
    while left < right:
        while s[left] not in vowels:
            left += 1
        while s[right] not in vowels:
            right -= 1
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return "".join(s)

```

Explanation:

We can reverse the vowels of a given string by following these steps:

1. Create a string `vowels` that contains all the vowels.
2. Convert the input string into a list of characters. This will allow us to modify the string in place.
3. Initialize two pointers, one at the start of the string (`left`) and one at the end of the string (`right`).
4. While the `left` pointer is less than the `right` pointer, perform the following steps:
   - Move the `left` pointer to the right until it reaches a vowel.
   - Move the `right` pointer to the left until it reaches a vowel.
   - Swap the characters at the `left` and `right` pointers.
   - Increment the `left` pointer and decrement the `right` pointer.
5. Once the `left` pointer is greater than or equal to the `right` pointer, the vowels have been reversed and we can join the characters back into a string and return it.

In the provided code, the `reverse_vowels` function implements these steps and returns the reversed string. The `while` loop ensures that the vowels are reversed correctly, and the `join` method is used to convert the list of characters back into a string.

To test the function, you can use the `assert` statement to check if the result of `reverse_vowels` is equal to the expected output for the given test case.

Overall, this function effectively reverses only the vowels of a given string while keeping all other characters intact.

Note: