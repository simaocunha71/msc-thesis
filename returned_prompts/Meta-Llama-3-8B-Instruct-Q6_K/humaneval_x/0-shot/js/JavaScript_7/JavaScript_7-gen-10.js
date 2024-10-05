```javascript
const filterBySubstring = (strings, substring) => {
  return strings.filter(str => str.includes(substring));
};
```



Explanation:

*   The `filterBySubstring` function takes two parameters: `strings` (an array of strings) and `substring` (a string to search for).
*   The function uses the `filter` method to create a new array with only the strings that contain the given `substring`.
*   The callback function `str => str.includes(substring)` is used to filter the strings. It returns `true` if the string `str` includes the `substring`, and `false` otherwise.
*   The resulting array of filtered strings is returned by the function.