```
const flipCase = (string) => {
  return string.split('').map((char) => char.charCodeAt(0) >= 65 && char.charCodeAt(0) <= 90 ? String.fromCharCode(char.charCodeAt(0) + 32) : String.fromCharCode(char.charCodeAt(0) - 32)).join('');
};
```


Explanation:

1. `split('')` splits the string into an array of individual characters.
2. `map()` applies a function to each character in the array.
3. `charCodeAt(0)` gets the Unicode code point of the character. For ASCII characters, this is equivalent to the ASCII code.
4. `>= 65 && <= 90` checks if the character is uppercase (A-Z). If true, add 32 to the code point to convert it to lowercase (a-z).
5. `String.fromCharCode()` converts the code point back to a character.
6. `join('')` combines the modified characters back into a string.

Test:
```
console.log(flipCase('Hello')); // Output: 'hELLO'
```


Note: This solution works for ASCII characters only. For non-ASCII characters, you may need to use a more advanced approach.