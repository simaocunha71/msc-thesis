
To solve this Kata, you should:

1. Create a function named `filterBySubstring` that takes two parameters:
- `strings`: an array of strings.
- `substring`: a string that you want to filter by.
2. Inside the function, create an empty array named `result`.
3. Iterate over the `strings` array using the `forEach()` function. For every string in the array, check if the `substring` is present in that string. If it is, add that string to the `result` array.
4. Return the `result` array when the iteration is done.

Here's the code to solve this Kata:

```javascript
const filterBySubstring = (strings, substring) => {
  const result = [];
  strings.forEach(string => {
    if (string.includes(substring)) {
      result.push(string);
    }
  });
  return result;
};
```

For the given tests:

- When `strings` is an empty array and `substring` is 'a', the function should return an empty array. This is because there are no strings to filter.
- When `strings` is `['abc', 'bacd', 'cde', 'array']` and `substring` is 'a', the function should return `['abc', 'bacd', 'array']`. This is because only these three strings contain the substring 'a'.

Here are the test cases for the solution:

```javascript
console.log(filterBySubstring([], 'a'));  // []
console.log(filterBySubstring(['abc', 'bacd', 'cde', 'array'], 'a'));  // ['abc', 'bacd', 'array']
```

These test cases will check if the function correctly filters the input list of strings based on the given substring.

To complete this Kata, you need to implement the `filterBySubstring` function and pass the provided test cases.

Happy coding!

/* Filter an input list of strings only for ones that contain given substring
  >>> filterBySubstring([], 'a')
  []
  >>> filterBySubstring(['abc', 'bacd', 'cde', '