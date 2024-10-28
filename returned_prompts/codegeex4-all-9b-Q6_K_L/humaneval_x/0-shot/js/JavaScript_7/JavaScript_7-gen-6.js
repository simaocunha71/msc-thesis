You can solve this problem by using the `filter` method in JavaScript. This method creates a new array with all elements that pass the test implemented by the provided function. In this case, the test is checking if the given substring is contained in the current string.

Here's the solution:

```javascript
const filterBySubstring = (strings, substring) => {
  return strings.filter(string => string.includes(substring));
}
```

This function takes two parameters: `strings`, which is the list of strings to filter, and `substring`, which is the substring to search for. It returns a new array containing only the strings that include the given substring.