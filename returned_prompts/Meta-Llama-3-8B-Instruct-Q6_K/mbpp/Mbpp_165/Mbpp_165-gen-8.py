```
def count_char_position(s):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    s = s.lower()
    count = 0
    for i in range(len(s)):
        if s[i] in alphabet and i == alphabet.index(s[i]):
            count += 1
    return count
```


The function `count_char_position` takes a string `s` as input and returns the number of characters in `s` that occur at the same position in `s` as in the English alphabet (case insensitive).

The function first converts the input string to lowercase using the `lower()` method. Then, it initializes a counter `count` to 0.

It then iterates over the characters in the string using a for loop. For each character, it checks if the character is in the English alphabet (case insensitive) and if its position in the string is the same as its position in the alphabet. If both conditions are true, it increments the `count` by 1.

Finally, the function returns the `count` which is the number of characters in the string that occur at the same position in the string as in the English alphabet.

The unit test `assert count_char_position("xbcefg") == 2` ensures that the function returns the correct count for the input string "xbcefg". The expected output is 2 because the characters 'b' and 'c' occur at the same position in the string as in the English alphabet.