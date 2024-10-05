```javascript
const filterByPrefix = (strings, prefix) => strings.filter(s => s.startsWith(prefix));
```
Explanation:
The `filter()` method creates a new array with all elements that pass the test implemented by the provided function. In this case, the function `s => s.startsWith(prefix)` checks if a string `s` starts with the given `prefix`. The `startsWith()` method returns a boolean indicating whether the string starts with the specified prefix.

This implementation is concise and efficient, as it uses the built-in `filter()` and `startsWith()` methods, which are optimized for performance. It also clearly expresses the intention of filtering the input list of strings based on the prefix.