Here is a solution using a stack to keep track of the opening and closing parentheses:

```javascript
const parseNestedParens = (paren_string) => {
  const groups = paren_string.split(' ');
  const result = [];

  for (const group of groups) {
    const stack = [];
    let maxDepth = 0;

    for (const char of group) {
      if (char === '(') {
        stack.push(char);
        maxDepth = Math.max(maxDepth, stack.length);
      } else if (char === ')') {
        stack.pop();
      }
    }

    result.push(maxDepth);
  }

  return result;
};

// Test
console.log(parseNestedParens('(()()) ((())) () ((())()())')); // Output: [2, 3, 1, 3]
```

The idea is to iterate through each group, and for each group, use a stack to keep track of the opening parentheses. Each time we encounter a closing parenthesis, we pop the opening parenthesis from the stack. The maximum depth of the stack at any point is the maximum level of nesting for that group. We add this value to the result array.

This solution has a time complexity of O(n), where n is the total number of characters in the input string, because we iterate through each character once. The space complexity is O(n) as well, because in the worst case, the stack can grow up to the size of the input string.