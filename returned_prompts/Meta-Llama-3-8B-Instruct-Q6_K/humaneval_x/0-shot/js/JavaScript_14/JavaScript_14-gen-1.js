Here is the solution:
```
const allPrefixes = (string) => {
  const prefixes = [];
  for (let i = 1; i <= string.length; i++) {
    prefixes.push(string.substring(0, i));
  }
  return prefixes;
};

console.log(allPrefixes('abc')); // ['a', 'ab', 'abc']
```
Explanation:

* We create an empty array `prefixes` to store the prefixes.
* We loop through the string from `i = 1` to `i = string.length` (inclusive).
* Inside the loop, we use the `substring` method to extract the prefix of length `i` from the original string, and push it to the `prefixes` array.
* Finally, we return the `prefixes` array.

This solution has a time complexity of O(n), where n is the length of the input string, because we iterate through the string once. The space complexity is O(n) as well, because we store all the prefixes in the `prefixes` array.