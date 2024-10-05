```
const allPrefixes = (string) => {
  const result = [];
  for (let i = 1; i <= string.length; i++) {
    result.push(string.substring(0, i));
  }
  return result;
};
```


Explanation:

*   The function `allPrefixes` takes a string as input.
*   It initializes an empty array `result` to store the prefixes.
*   It iterates over the string using a for loop, starting from 1 (since the empty string is a prefix) to the length of the string.
*   In each iteration, it uses the `substring` method to extract the prefix of the current length and adds it to the `result` array.
*   Finally, it returns the `result` array containing all the prefixes of the input string, from shortest to longest.

Example:

```
console.log(allPrefixes('abc')); // Output: ['a', 'ab', 'abc']
```


This function has a time complexity of O(n), where n is the length of the input string, since it iterates over the string once. It has a space complexity of O(n) as well, since it stores all the prefixes in the `result` array.