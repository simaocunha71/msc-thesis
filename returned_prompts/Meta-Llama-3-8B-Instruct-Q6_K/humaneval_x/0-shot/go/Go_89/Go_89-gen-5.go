Explanation:
The function Encrypt takes a string as an argument and returns a new string where the alphabet has been rotated down by two multiplied by two places.

The function works by iterating over each character in the input string. If the character is a letter (either lowercase or uppercase), it calculates the new character by shifting the ASCII value down by two multiplied by two places. This is done using the modulo operator (`%`) to ensure that the result is still within the range of the alphabet.

For example, the letter 'a' has an ASCII value of 97. Shifting it down by two multiplied by two places would result in the ASCII value 103, which corresponds to the letter 'm'. Similarly, the letter 'A' has an ASCII value of 65, which shifted down by two multiplied by two places would result in the ASCII value 71, which corresponds to