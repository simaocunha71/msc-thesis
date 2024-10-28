```
def remove_vowels(text):
    vowels = 'aeiouAEIOU'
    result = ''
    for char in text:
        if char not in vowels:
            result += char
    return result
```


Explanation:
The function `remove_vowels` takes a string `text` as input and returns a new string with all vowels removed. It uses a string `vowels` to store all the vowels (both lowercase and uppercase). It then iterates over each character `char` in the input string using a for loop. If the character is not a vowel (i.e., it's not in the `vowels` string), it adds the character to the result string. Finally, it returns the result string.

The unit tests provided ensure that the function works correctly in different scenarios, such as:

* An empty string
* A string with a mix of letters and newline characters
* A string with only vowels
* A string with a mix of letters and uppercase vowels
* A string with only consonants

These tests help to verify that the function is working correctly and that it handles different edge cases.