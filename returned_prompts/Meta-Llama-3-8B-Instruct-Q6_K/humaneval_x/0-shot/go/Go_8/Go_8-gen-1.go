Here is the solution in JavaScript:

```javascript
const countDistinctCharacters = (string) => {
  const charSet = new Set();
  for (let i = 0; i < string.length; i++) {
    const char = string[i].toLowerCase();
    charSet.add(char);
  }
  return charSet.size;
};

console.log(countDistinctCharacters('xyzXYZ')); // Output: 3
console.log(countDistinctCharacters('Jerry')); // Output: 4
```
In this solution, we create a Set (a collection of unique values) to store the distinct characters. We iterate over the input string, convert each character to lowercase (to ignore case), and add it to the Set. Finally, we return the size of the Set, which represents the number of distinct characters. This approach has a time complexity of O(n), where n is the length of the input string.