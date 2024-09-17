```
def count_char_position(s):
    count = 0
    for i in range(len(s)):
        if s[i].lower() == chr(ord('a') + i):
            count += 1
    return count
```


In this problem, we need to write a function that counts the number of characters in a given string that occur at the same position as in the English alphabet (case insensitive). For example, the string "xbcefg" should return 2 because 'b' and 'c' are at the same position as in the English alphabet.

To solve this problem, we iterate over each character in the string using a for loop. For each character, we convert it to lowercase and check if it is equal to the character at the same position in the English alphabet. We do this by using the `ord` function to get the ASCII value of 'a' and adding the current position `i` to it. Then, we convert this ASCII value back to a character using the `chr` function.

If the character is equal to the character at the same position in the English alphabet, we increment the count. Finally, we return the count.

The unit test `assert count_char_position("xbcefg") == 2` helps to clarify the problem by providing an example of the expected output. This test shows that the function should return 2 for the input "xbcefg", which means that 'b' and 'c' are the only characters that occur at the same position as in the English alphabet.