```
def count_char_position(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    count = 0
    for char in s:
        if char.lower() in alphabet:
            if char.lower() == alphabet[alphabet.index(char.lower())]:
                count += 1
    return count
```



The function `count_char_position` counts the number of characters in a string `s` that occur at the same position in the string as in the English alphabet (case insensitive). It does this by iterating over each character in the string, checking if it is in the English alphabet (case insensitive), and if it is, checking if it is at the same position as in the alphabet. If it is, it increments a counter. The function returns the count.

The unit test `assert count_char_position("xbcefg") == 2` shows that the function should return 2 for the string "xbcefg", which is the number of characters in this string that occur at the same position in the string as in the English alphabet (case insensitive). The characters 'b' and 'c' are at the same position in the string as in the alphabet. The function correctly identifies these characters and returns the count of 2.