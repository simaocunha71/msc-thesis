Here is the solution using a Set in JavaScript:
```
const countDistinctCharacters = (string) => {
  const charSet = new Set();
  for (let char of string.toLowerCase()) {
    charSet.add(char);
  }
  return charSet.size;
};
```
Explanation:

1. We create a new Set called `charSet`.
2. We iterate over the characters in the input string, converting each character to lowercase using the `toLowerCase()` method.
3. We add each character to the `charSet`.
4. Finally, we return the size of the `charSet`, which represents the number of distinct characters in the input string.

You can test this function with the examples you provided:
```
console.log(countDistinctCharacters('xyzXYZ')); // Output: 3
console.log(countDistinctCharacters('Jerry')); // Output: 4
```
This solution has a time complexity of O(n), where n is the length of the input string, since we are iterating over the characters in the string once. The space complexity is also O(n), since we are storing at most n characters in the Set.