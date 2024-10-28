```javascript
const filterBySubstring = (strings, substring) => strings.filter(str => str.includes(substring));
```


Explanation:
The provided problem is asking to create a function `filterBySubstring` that takes two parameters: an array of strings `strings` and a substring `substring`. This function should return a new array containing only the strings from the original array that contain the given substring.

The solution uses the built-in `filter()` method of JavaScript arrays. This method creates a new array with all elements that pass the test implemented by the provided function.

The function passed to `filter()` checks if each string in the array includes the given substring using the `includes()` method. If a string includes the substring, it is included in the new array. Otherwise, it is excluded.

For example, if we call `filterBySubstring(['abc', 'bacd', 'cde', 'array'], 'a')`, the function will return `['abc', 'bacd', 'array']` because these are the strings that include the substring `'a'`. If we call `filterBySubstring([], 'a')`, the function will return an empty array because there are no strings in the input array that include the substring `'a'`.