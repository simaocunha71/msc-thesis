To solve this problem, first, we need to identify the opening and closing parentheses and split the string accordingly.
Here's a step-by-step breakdown of the solution:

1. Initialize an empty array called `result` to store the separated groups.
2. Initialize an empty string variable called `currentGroup` to keep track of the current group of parentheses.
3. Iterate over each character in the `paren_string` using a for loop.
   a. If the current character is an opening parenthesis (i.e., '('), append an empty string to the `currentGroup` variable.
   b. If the current character is a closing parenthesis (i.e., ')'), push the `currentGroup` to the `result` array and reset the `currentGroup` to an empty string.
   c. If the current character is a space, do nothing as we need to ignore any spaces.
   d. Otherwise, append the current character to the `currentGroup`.
4. After the loop, if there are any remaining characters in the `currentGroup`, push it to the `result` array.
5. Return the `result` array containing all the separated groups.

Here's the implementation of the solution in JavaScript:

```javascript
const separateParenGroups = (paren_string) => {
  const result = [];
  let currentGroup = '';

  for (let i = 0; i < paren_string.length; i++) {
    const char = paren_string[i];

    if (char === '(') {
      currentGroup = '';
    } else if (char === ')') {
      result.push(currentGroup);
      currentGroup = '';
    } else if (char === ' ') {
      continue;
    } else {
      currentGroup += char;
    }
  }

  if (currentGroup.length > 0) {
    result.push(currentGroup);
  }

  return result;
};
```

This implementation correctly separates the groups of nested parentheses from the input string while ignoring any spaces. It returns an array containing all the separated groups in the order they appear in the input string.

To test the solution, you can use the provided test case:

