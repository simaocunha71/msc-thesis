```
def count_upper(s):
    count = 0
    for i in range(0, len(s), 2):
        if s[i].upper() in 'AEIOU':
            count += 1
    return count
```


Explanation:

1. We initialize a variable `count` to 0, which will store the count of uppercase vowels in even indices.
2. We iterate over the string `s` using a for loop, starting from index 0 and incrementing by 2 each time (using the range function with step size 2).
3. Inside the loop, we check if the character at the current index `i` is an uppercase vowel by using the `upper()` method to convert the character to uppercase and checking if it is in the string 'AEIOU' (which contains all uppercase vowels).
4. If the character is an uppercase vowel, we increment the `count` variable by 1.
5. Finally, we return the `count` variable, which represents the number of uppercase vowels in even indices.

For example, when we call `count_upper('aBCdEf')`, the loop iterates over the string as follows:

1. `i` is 0, `s[i]` is 'a', which is not an uppercase vowel, so `count` remains 0.
2. `i` is 2, `s[i]` is 'C', which is an uppercase vowel, so `count` becomes 1.
3. `i` is 4, `s[i]` is 'f', which is not an uppercase vowel, so `count` remains 1.

The function returns `count`, which is 1 in this case. Similarly, for `count_upper('abcdefg')`, the function returns 0, and for `count_upper('dBBE')`, the function returns 0.