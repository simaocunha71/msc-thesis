```javascript
const filterBySubstring = (strings, substring) => strings.filter(str => str.includes(substring));

// Test cases
console.log(filterBySubstring([], 'a')); // []
console.log(filterBySubstring(['abc', 'bacd', 'cde', 'array'], 'a')); // ['abc', 'bacd', 'array']
```

Explanation:
The problem requires you to create a function that filters a list of strings and returns a new list containing only the strings that include a specific substring. The function should take two parameters: the list of strings and the substring to search for.

The solution uses the built-in `filter()` method of JavaScript arrays, which creates a new array with all elements that pass the test implemented by the provided function. In this case, the function checks if each string includes the given substring using the `includes()` method. If a string includes the substring, it is included in the new array; otherwise, it is excluded.

The test cases demonstrate the correct behavior of the function. When called with an empty list and a substring, the function returns an empty list. When called with a list containing strings that include the substring and a list that does not, the function returns the expected results.