```
const filterByPrefix = (strings, prefix) => strings.filter(str => str.startsWith(prefix));
```
Explanation:
The `filter()` method creates a new array with all elements that pass the test implemented by the provided function. In this case, the function checks if the string starts with the given prefix using the `startsWith()` method. This method returns `true` if the string begins with the specified characters, and `false` otherwise. The `filter()` method will return an array of all strings that start with the given prefix. If no strings match the prefix, an empty array will be returned.