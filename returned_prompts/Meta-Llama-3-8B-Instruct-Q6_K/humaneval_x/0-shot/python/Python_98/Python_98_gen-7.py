```
def count_upper(s):
    count = 0
    for i, char in enumerate(s):
        if i % 2 == 0 and char in 'AEIOU':
            if char.isupper():
                count += 1
    return count
```


This function uses a for loop to iterate over the string `s`. The `enumerate` function is used to get both the index `i` and the character `char` of the string. The condition `i % 2 == 0` checks if the index is even. The condition `char in 'AEIOU'` checks if the character is a vowel. The condition `char.isupper()` checks if the vowel is uppercase. If all conditions are met, the `count` variable is incremented by 1. Finally, the function returns the `count` variable.

For example, if we call `count_upper('aBCdEf')`, the function will iterate over the string and find that the character 'B' is an uppercase vowel at an even index, so the function will return 1. If we call `count_upper('abcdefg')`, the function will not find any uppercase vowels at even indices, so the function will return 0. If we call `count_upper('dBBE')`, the function will find that the character 'B' is an uppercase vowel at an even index, but it will also find that the character 'B' is not a vowel, so the function will return 0.