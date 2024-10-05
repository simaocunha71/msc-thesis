  return string.length;
}

This problem is asking to create a function called `strlen` that takes a string as an argument and returns the length of the string. The length of a string is the number of characters it contains.

The problem provides two examples of how the function should work: `strlen('')` should return `0` because the empty string has no characters, and `strlen('abc')` should return `3` because the string `'abc'` has 3 characters.

The solution is to use the built-in `length` property of strings in JavaScript. This property returns the number of characters in the string. So, the `strlen` function can simply return the `length` property of the input string.

Here's the solution:
```
const strlen = (string) => {
  return string.length;
}
```
This function takes a string as an argument and returns its length. For example, `strlen('')` would return `0` and `strlen('abc')` would return `3`.