```
  return a.split('').map((x, i) => x ^ b[i % b.length]).join('');
```
Here's an explanation of the code:

*   We use the `split` method to split the strings `a` and `b` into arrays of individual characters.
*   We use the `map` method to iterate over the characters in `a`. For each character, we use the ternary operator (`x ^ b[i % b.length]`) to perform a binary XOR operation with the corresponding character in `b`. If `b` is shorter than `a`, we use the modulus operator (`i % b.length`) to wrap around to the start of `b` when `i` exceeds the length of `b`.
*   We use the `join` method to concatenate the resulting characters back into a string.

This code assumes that the input strings `a` and `b` consist only of 1s and 0s. If the input strings can contain other characters, you may need to add error handling or modify the code to handle those characters correctly.