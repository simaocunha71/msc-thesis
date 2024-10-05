```
const filterBySubstring = (strings, substring) => strings.filter(str => str.includes(substring));
```


Explanation:
The `filterBySubstring` function takes two parameters, `strings` and `substring`. It uses the `filter` method on the `strings` array to create a new array with only the elements that pass the test implemented by the provided function.

The provided function, `str => str.includes(substring)`, checks if the current string `str` includes the `substring`. If it does, the function returns `true`, and the string is included in the new array. If it doesn't, the function returns `false`, and the string is excluded from the new array.

The function then returns the new array containing only the strings that include the `substring`. If the `strings` array is empty, the function returns an empty array. If the `substring` is not found in any of the strings, the function also returns an empty array. If the `substring` is found in some of the strings, the function returns an array containing those strings.