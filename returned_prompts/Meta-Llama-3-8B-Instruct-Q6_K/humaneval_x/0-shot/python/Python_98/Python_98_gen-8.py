```
def count_upper(s):
    count = 0
    for i in range(0, len(s), 2):
        if s[i].upper() in 'AEIOU':
            count += 1
    return count
```


Explanation:
The function `count_upper(s)` takes a string `s` as input and returns the count of uppercase vowels at even indices. 

The function iterates over the string with a step size of 2 using `range(0, len(s), 2)`, which gives us the even indices.

For each even index `i`, it checks if the character at that index `s[i]` is an uppercase vowel by converting it to uppercase using `s[i].upper()` and checking if it is in the string 'AEIOU'. If it is, it increments the count.

Finally, the function returns the count. 

For example, if the input is 'aBCdEf', the function will return 1 because there is one uppercase vowel 'C' at an even index. If the input is 'abcdefg', the function will return 0 because there are no uppercase vowels at even indices. If the input is 'dBBE', the function will return 0 because there are no uppercase vowels at even indices. 