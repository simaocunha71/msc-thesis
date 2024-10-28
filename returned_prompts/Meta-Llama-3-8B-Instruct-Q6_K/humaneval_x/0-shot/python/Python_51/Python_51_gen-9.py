```
def remove_vowels(text):
    vowels = 'aeiouAEIOU'
    return ''.join([char for char in text if char not in vowels])
```


Explanation:
The remove_vowels function takes a string as input and returns a new string with all the vowels removed. It uses a list comprehension to iterate over each character in the input string. For each character, it checks if the character is not in the string of vowels. If it's not a vowel, it includes it in the new string. Finally, it uses the join function to concatenate all the characters in the list into a single string. This string is then returned as the result.