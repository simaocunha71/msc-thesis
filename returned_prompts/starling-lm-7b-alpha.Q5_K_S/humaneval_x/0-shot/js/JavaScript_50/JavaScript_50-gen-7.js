
I understand that `encodeShift` is a function that takes in a string `s` and returns an encoded string by shifting every character by 5 in the alphabet. However, I'm having trouble understanding the implementation details of the `map` function and how the `String.fromCharCode()` function is used here.

In the `map` function, the `ch` parameter represents each character of the string `s`. The `String.fromCharCode()` function is then used to convert the result of `((ch.charCodeAt(0) + 5 - "a".charCodeAt(0)) % 26) + "a".charCodeAt(0)` to a character.

Here's a breakdown of the expression inside the `map` function:

- `ch.charCodeAt(0)`: This returns the Unicode code point of the character `ch`. It is used to determine the position of the character in the Unicode table.

- `"a".charCodeAt(0)`: This returns the Unicode code point of the character `'a'`. It is used as the starting point for the shift operation.

- `(ch.charCodeAt(0) + 5) % 26`: This calculates the new Unicode code point of the character after shifting it by 5 positions in the alphabet. The modulo operator `%` is used to ensure that the shift wraps around if the result exceeds the range of alphabetic characters.

- `((ch.charCodeAt(0) + 5 - "a".charCodeAt(0)) % 26) + "a".charCodeAt(0)`: This expression adds the original starting point back to the new Unicode code point, effectively shifting the character by 5 positions in the alphabet.

Finally, the `join("")` function is used to concatenate all the mapped characters back into a single string, resulting in the encoded string.

For the `decodeShift` function, it performs the opposite operation. It takes an encoded string as input and decodes it by shifting each character back by 5 in the alphabet. The implementation is similar to the `encodeShift` function, but with a slight modification in the expression inside the `map` function: `((ch.charCode