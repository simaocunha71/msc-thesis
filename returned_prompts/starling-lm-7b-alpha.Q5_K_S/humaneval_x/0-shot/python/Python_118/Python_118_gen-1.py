# Here's a step-by-step solution to the problem:

1. Create a dictionary of vowels and their corresponding lower-case and upper-case versions. 
   Example: {'a': 'a', 'e': 'e', 'i': 'i', 'o': 'o', 'u': 'u'}

2. Initialize a variable `closest_vowel` to store the closest vowel found. Set its initial value to an empty string.

3. Iterate through each letter in the word from left to right, starting from the second letter.

4. For each letter, check if it is a consonant and if the next letter is a vowel.

5. If the current letter is a consonant and the next letter is a vowel, update the `closest_vowel` variable with the current letter. 
   If the current letter is a consonant and the next letter is not a vowel, continue to the next iteration.

6. After iterating through all the letters, check if the `closest_vowel` variable is still an empty string. If it is, return the empty string.

7. If the `closest_vowel` variable is not empty, return the lower-case version of the closest vowel using the dictionary created in step 1.

Here's the Python code that implements the above steps:

```python
def get_closest_vowel(word):
    vowels = {'a': 'a', 'e': 'e', 'i': 'i', 'o': 'o', 'u': 'u'}
    closest_vowel = ''

    for idx, letter in enumerate(word):
        if idx > 0 and idx < len(word) - 1 and letter.isalpha() and letter.lower() not in vowels:
            continue
        elif letter.isalpha() and word[idx + 1].lower() in vowels:
            closest_vowel = letter.lower()
            break

    return closest_vowel
```

This implementation has a time complexity of O(n), where n is the length of the input word.

It's important to note that