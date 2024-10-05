Here's how you might do it in JavaScript:

```javascript
const filterByPrefix = (strings, prefix) => {
  return strings.filter(string => string.startsWith(prefix));
}
```

This function uses the `filter` method on the `strings` array, which creates a new array with all elements that pass the test implemented by the provided function. The `startsWith` method is used to test if each string starts with the given `prefix`.