```javascript
const filterBySubstring = (strings, substring) => strings.filter(str => str.includes(substring));
```


Explanation:
The `filterBySubstring` function takes two parameters: `strings` (an array of strings) and `substring` (the substring to search for). It uses the `filter` method to create a new array with only the strings that contain the `substring`. The `includes` method is used to check if a string contains the `substring`. If the string contains the `substring`, it is included in the new array; otherwise, it is excluded. The resulting array is then returned.