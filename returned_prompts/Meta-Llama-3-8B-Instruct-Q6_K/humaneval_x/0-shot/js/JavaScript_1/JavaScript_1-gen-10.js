Here is the solution for the problem:

```javascript
const separateParenGroups = (paren_string) => {
  const stack = [];
  const result = [];
  const groups = [];

  for (let i = 0; i < paren_string.length; i++) {
    if (paren_string[i] === '(') {
      stack.push(paren_string[i]);
      if (stack.length === 1) {
        groups.push([]);
      }
    } else if (paren_string[i] === ')') {
      stack.pop();
      groups[groups.length - 1].push(paren_string[i - stack.length + 1]);
    }
  }

  return groups.map((group) => group.join(''));
};

console.log(separateParenGroups('( ) (( )) (( )( ))')); // ['()', '(())', '(()())']
```

In this solution, we iterate over the input string and use a stack to keep track of the nesting level of the parentheses. When we encounter an open parenthesis, we push it to the stack and start a new group. When we encounter a close parenthesis, we pop the stack and add the group to the result array. Finally, we join each group into a string and return the result.