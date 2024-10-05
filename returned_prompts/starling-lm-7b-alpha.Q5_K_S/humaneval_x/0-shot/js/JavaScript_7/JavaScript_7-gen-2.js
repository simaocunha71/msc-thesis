Here's a solution that uses the `filter()` method to create a new array containing only the strings that include the given substring:

```javascript
const filterBySubstring = (strings, substring) => {
  return strings.filter(str => str.includes(substring));
};
```

In this solution, the `filter()` method is called on the `strings` array. For each string in the array, the arrow function `str => str.includes(substring)` is evaluated. If the string includes the given substring, the arrow function returns `true`, and the string is included in the new array. If the string does not include the substring, the arrow function returns `false`, and the string is excluded from the new array. The `filter()` method then collects all the strings for which the arrow function returned `true` into a new array, which is returned as the final result.

This solution will correctly filter an input list of strings based on whether they contain a given substring.

Here are some test cases to demonstrate the solution:

```javascript
console.log(filterBySubstring([], 'a')); // []
console.log(filterBySubstring(['abc', 'bacd', 'cde', 'array'], 'a')); // ['abc', 'bacd', 'array']
```

The first test case checks if an empty array is correctly filtered for the substring 'a'. It should return an empty array, as there are no strings to filter. The second test case checks if an array containing various strings is correctly filtered for the substring 'a'. It should return `['abc', 'bacd', 'array']`, as these are the only strings in the array that include the substring 'a'.

Overall, this solution provides a straightforward and efficient way to filter an array of strings based on whether they contain a specific substring.































































































