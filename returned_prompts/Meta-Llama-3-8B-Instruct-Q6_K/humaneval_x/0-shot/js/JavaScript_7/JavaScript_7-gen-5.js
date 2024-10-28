```javascript
const filterBySubstring = (strings, substring) => strings.filter(str => str.includes(substring));

// Test cases
console.log(filterBySubstring([], 'a')); // []
console.log(filterBySubstring(['abc', 'bacd', 'cde', 'array'], 'a')); // ['abc', 'bacd', 'array']
``` 