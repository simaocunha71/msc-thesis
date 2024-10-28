```
def remove_vowels(text):
    vowels = 'aeiouAEIOU'
    return ''.join([char for char in text if char not in vowels])
```



This function works by iterating over each character in the input string. If the character is not a vowel (i.e., it is not in the string 'aeiouAEIOU'), it is included in the output string. The `join` function is used to concatenate the characters that are not vowels into a single string. The function returns this string, which is the input string with all vowels removed.