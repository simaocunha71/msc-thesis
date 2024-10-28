```
const decodeShift = (s) => {
  return s.split("").map(ch => String.fromCharCode(
    ((ch.charCodeAt(0) - "a".charCodeAt(0) + 26) % 26) + "a".charCodeAt(0)
  )).join("");
}
```


Explanation:

1. `encodeShift` function takes a string `s` as input and returns the encoded string. It works by shifting every character by 5 in the alphabet. Here's a step-by-step breakdown:

    - `s.split("")` splits the input string into an array of individual characters.
    - `map` is used to apply the encoding function to each character.
    - The encoding function is `String.fromCharCode((ch.charCodeAt(0) + 5 - "a".charCodeAt(0)) % 26) + "a".charCodeAt(0)`. It works as follows:
      - `ch.charCodeAt(0)` gets the ASCII code of the character.
      - `+ 5 - "a".charCodeAt(0)` shifts the code by 5 positions in the alphabet. For example, 'a' becomes 'f'.
      - `% 26` ensures that the shift wraps around the alphabet (e.g., 'z' becomes 'e').
      - `+ "a".charCodeAt(0)` converts the shifted code back to a character.
    - `join("")` combines the encoded characters back into a string.

2. `decodeShift` function takes an encoded string `s` as input and returns the decoded string. It works by reversing the encoding process. Here's a step-by-step breakdown:

    - `s.split("")` splits the input string into an array of individual characters.
    - `map` is used to apply the decoding function to each character.
    - The decoding function is `String.fromCharCode((ch.charCodeAt(0) - "a".charCodeAt(0) + 26) % 26) + "a".charCodeAt(0)`. It works as follows:
      - `ch.charCodeAt(0)` gets the ASCII code of the character.
      - `- "a".charCodeAt(0)` shifts the code in the opposite direction of the encoding process (i.e., -5).
      - `% 26` ensures that the shift wraps around the alphabet (e.g., 'f' becomes 'a').
      - `+ "a".charCodeAt(0)` converts the decoded code back to a character.
    -