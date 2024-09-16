```python
def reverse_vowels(my_string):
    vowels = "aeiou"
    vowel_indexes = [i for i, char in enumerate(my_string) if char in vowels]
    for i in range(len(vowel_indexes) - 1):
        my_string = my_string[:vowel_indexes[i]] + my_string[vowel_indexes[i]].lower() + my_string[vowel_indexes[i] + 1:]
    return my_string
```
