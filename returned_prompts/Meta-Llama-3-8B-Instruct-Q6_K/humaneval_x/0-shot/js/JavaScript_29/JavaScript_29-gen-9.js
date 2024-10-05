```javascript
const filterByPrefix = (strings, prefix) => strings.filter(str => str.startsWith(prefix));
```
Explanation:
The `filterByPrefix` function takes two arguments: `strings` (an array of strings) and `prefix` (a string). It uses the `filter` method to create a new array with only the strings that start with the given `prefix`. The `filter` method takes a callback function as its argument, which is called for each element in the `strings` array. The callback function returns `true` if the string starts with the `prefix`, and `false` otherwise. The `startsWith` method is used to check if a string starts with a given prefix. The resulting array of filtered strings is then returned.