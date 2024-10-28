```
  return [...new Set(string.split('').map((char, index) => string.slice(0, index+1)))].sort((a, b) => a.length - b.length);
```
Explanation:

1. `string.split('')` splits the input string into an array of individual characters.
2. `map((char, index) => string.slice(0, index+1))` maps each character to the corresponding prefix of the string. `string.slice(0, index+1)` returns a substring starting from the beginning of the string and ending at the current index (inclusive).
3. `Set` is used to remove duplicates from the array of prefixes.
4. `sort((a, b) => a.length - b.length)` sorts the prefixes in ascending order of their lengths.

Example: `allPrefixes('abc')` will return `['a', 'ab', 'abc']`.