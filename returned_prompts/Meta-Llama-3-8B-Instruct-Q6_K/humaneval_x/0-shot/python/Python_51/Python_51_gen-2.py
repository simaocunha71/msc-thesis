```
def remove_vowels(text):
    vowels = 'aeiouAEIOU'
    return ''.join([char for char in text if char not in vowels])
```


This function works by iterating over each character in the input string, and checking if the character is a vowel (using the set of vowels defined as a string). If the character is not a vowel, it is included in the output string. The output string is then returned.

The unit test cases provided ensure that the function correctly handles various edge cases, including:

* An empty input string
* A string with a mix of uppercase and lowercase letters
* A string with only vowels
* A string with only consonants
* A string with both vowels and consonants

The function also correctly handles newline characters in the input string.