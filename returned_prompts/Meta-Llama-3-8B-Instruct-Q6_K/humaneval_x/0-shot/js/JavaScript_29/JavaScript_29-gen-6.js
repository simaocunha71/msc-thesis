Here is a simple and efficient solution using the `filter()` method and a callback function:
```
const filterByPrefix = (strings, prefix) => strings.filter(str => str.startsWith(prefix));
```
Explanation:

* `strings.filter()` creates a new array with all elements that pass the test implemented by the provided callback function.
* The callback function `str => str.startsWith(prefix)` checks if each string `str` starts with the given `prefix` using the `startsWith()` method.
* If the string starts with the prefix, the callback function returns `true`, and the string is included in the resulting array. Otherwise, it returns `false`, and the string is excluded.

You can test this function with the provided examples:
```
console.log(filterByPrefix([], 'a')); // []
console.log(filterByPrefix(['abc', 'bcd', 'cde', 'array'], 'a')); // ['abc', 'array']
```
This solution has a time complexity of O(n), where n is the length of the input array, since we need to iterate over all elements to filter them. The `startsWith()` method has a constant time complexity, so it doesn't affect the overall time complexity. Space complexity is O(1) since we're only using a small amount of extra memory to store the filtered array.