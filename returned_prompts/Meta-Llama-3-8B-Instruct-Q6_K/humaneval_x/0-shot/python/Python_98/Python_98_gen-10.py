```
def count_upper(s):
    return sum(1 for i in range(0, len(s), 2) if s[i].upper() in 'AEIOU')
```
Explanation:
The function `count_upper(s)` takes a string `s` as input and returns the count of uppercase vowels in even indices.

The function uses a generator expression to iterate over the even indices of the string `s`. For each index `i`, it checks if the character at that index is an uppercase vowel by using the `in` operator to check if the character's uppercase equivalent is in the string 'AEIOU'. If it is, it counts it.

The `sum` function is used to sum up the counts for all even indices.

For example, for the input 'aBCdEf', the function will iterate over the even indices 0 and 2, and count the uppercase vowel 'C'. For the input 'abcdefg', it will not find any uppercase vowels. For the input 'dBBE', it will not find any uppercase vowels either. Therefore, the function returns 1, 0, and 0, respectively.