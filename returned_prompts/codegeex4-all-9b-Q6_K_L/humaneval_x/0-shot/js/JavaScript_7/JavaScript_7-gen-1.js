You can use the `filter` method in JavaScript to achieve this. Here's an example:

```javascript
const filterBySubstring = (strings, substring) => {
  return strings.filter(str => str.includes(substring));
};
```

This will return a new array containing only the strings that have the given substring.