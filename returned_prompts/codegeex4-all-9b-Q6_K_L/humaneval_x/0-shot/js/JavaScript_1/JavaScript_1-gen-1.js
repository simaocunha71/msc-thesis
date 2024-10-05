To solve this problem, we can use a stack to keep track of the parentheses we encounter as we iterate through the string. When we encounter an opening parenthesis, we push it onto the stack. When we encounter a closing parenthesis, we pop the stack and if the stack is empty, we know we've reached the end of a group of parentheses. We can then add this group to our result list.

Here's the complete solution:

```javascript
const separateParenGroups = (paren_string) => {
  const stack = [];
  const groups = [];
  let currentGroup = "";

  for (let i = 0; i < paren_string.length; i++) {
    const char = paren_string[i];

    if (char === "(") {
      stack.push(char);
      currentGroup += char;
    } else if (char === ")") {
      stack.pop();
      currentGroup += char;

      if (stack.length === 0) {
        groups.push(currentGroup);
        currentGroup = "";
      }
    }
  }

  return groups;
};
```

This solution should correctly separate the groups of parentheses in the input string and return the list of separate groups.