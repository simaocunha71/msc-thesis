```
def count_char_position(s):
    count = 0
    for i, c in enumerate(s.lower()):
        if c.isalpha() and c == chr(ord('a') + i):
            count += 1
    return count
```


This function iterates over each character in the input string, converts it to lowercase, and checks if it's an alphabetical character. If it is, it checks if the character is equal to the corresponding letter in the alphabet (using the `ord` function to get the ASCII value of 'a' and adding the index `i`). If the character matches, it increments the `count` variable. Finally, it returns the total count. The unit test `assert count_char_position("xbcefg") == 2` ensures that the function is working correctly.