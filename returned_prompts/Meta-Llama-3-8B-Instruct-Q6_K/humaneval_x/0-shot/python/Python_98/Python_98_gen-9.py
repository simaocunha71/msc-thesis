```
def count_upper(s):
    count = 0
    for i in range(len(s)):
        if i % 2 == 0 and s[i].upper() in 'AEIOU':
            count += 1
    return count
```


Note: The function `count_upper(s)` takes a string `s` as input and returns the count of uppercase vowels in even indices. The `range(len(s))` generates indices for the string, and the `if` statement checks if the current index is even (`i % 2 == 0`) and if the character at that index is an uppercase vowel (`s[i].upper() in 'AEIOU'`). The `count` variable is incremented whenever an uppercase vowel is found at an even index, and the final count is returned. 