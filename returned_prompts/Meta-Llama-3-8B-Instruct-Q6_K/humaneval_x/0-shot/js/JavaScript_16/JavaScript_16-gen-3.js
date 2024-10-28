```javascript
const countDistinctCharacters = (string) => {
  const charSet = new Set();
  for (let char of string.toLowerCase()) {
    charSet.add(char);
  }
  return charSet.size;
};
```
Explanation:
We use a Set to keep track of distinct characters in the string. We convert the string to lowercase to ignore the case sensitivity. We iterate over each character in the string, and add it to the Set. The size of the Set is the number of distinct characters. We return the size of the Set as the result.

For example, when we call `countDistinctCharacters('xyzXYZ')`, the Set will contain the characters 'x', 'y', and 'z', and the size of the Set will be 3. Similarly, when we call `countDistinctCharacters('Jerry')`, the Set will contain the characters 'j', 'e', 'r', and 'y', and the size of the Set will be 4.