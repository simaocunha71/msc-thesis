```javascript
const filterBySubstring = (strings, substring) => strings.filter(str => str.includes(substring));
```
Explanation:
The `filter()` function is used to create a new array with all elements that pass the test implemented by the provided function. In this case, the function checks if a string contains the given substring using the `includes()` method. If the string contains the substring, it is included in the new array; otherwise, it is not. The new array is then returned by the `filterBySubstring()` function.