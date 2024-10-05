```javascript
const string = string.toLowerCase();
let distinctCharacters = new Set();

for (let char of string) {
  distinctCharacters.add(char);
}

return distinctCharacters.size;
```
Explanation:
- We convert the input string to lowercase using the `toLowerCase()` method to ensure that the counting is case-insensitive.
- We create an empty Set object `distinctCharacters` to store the distinct characters.
- We iterate over each character in the string using the `for...of` loop.
- For each character, we add it to the `distinctCharacters` Set using the `add()` method.
- Finally, we return the size of the `distinctCharacters` Set, which represents the number of distinct characters in the string. The Set automatically eliminates duplicates, so we don't need to worry about counting them separately.

Example usage:
```javascript
console.log(countDistinctCharacters('xyzXYZ')); // Output: 3
console.log(countDistinctCharacters('Jerry')); // Output: 4
```javascript
```
Note: The `Set` data structure is used to automatically eliminate duplicates, making it a convenient and efficient way to count distinct characters.