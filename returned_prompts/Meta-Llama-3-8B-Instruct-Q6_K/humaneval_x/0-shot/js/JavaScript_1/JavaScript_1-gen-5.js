Here is the solution for the problem:

```javascript
const separateParenGroups = (paren_string) => {
  const stack = [];
  const groups = [];
  const group = [];

  for (let i = 0; i < paren_string.length; i++) {
    if (paren_string[i] === '(') {
      stack.push(paren_string[i]);
      group.push(paren_string[i]);
    } else if (paren_string[i] === ')') {
      if (stack.length > 0) {
        stack.pop();
        group.push(paren_string[i]);
      } else {
        groups.push(group.join(''));
        group = [];
      }
    }
  }

  if (stack.length > 0) {
    groups.push(group.join(''));
  }

  return groups;
};
```

This solution uses a stack to keep track of the opening parentheses and a variable `group` to build each group of parentheses. When a closing parenthesis is encountered, it checks if the stack is empty, which means it's the end of a group, and if so, it adds the current group to the list of groups and resets the current group. If the stack is not empty, it means it's still building the current group. At the end, it checks if there are any remaining characters in the stack, which means there's an unclosed group, and adds it to the list of groups. The function returns the list of groups.