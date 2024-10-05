Here is a function that separates groups of nested parentheses:

```javascript
function separateParenGroups(paren_string) {
  let stack = [];
  let result = [];
  for (let i = 0; i < paren_string.length; i++) {
    if (paren_string[i] === '(') {
      stack.push(i);
    } else if (paren_string[i] === ')') {
      if (stack.length) {
        result.push(paren_string.substring(stack.pop(), i + 1));
      }
    }
  }
  return result;
}
```

The function uses a stack to keep track of the opening brackets it encounters. When a closing bracket is encountered, it checks if the stack is not empty. If the stack is not empty, it means there is a corresponding opening bracket for the closing bracket, so it creates a substring from the opening bracket to the closing bracket (exclusive) and adds it to the result array. Then, it pops the opening bracket from the stack.

For example, when the input is `'(((())))'`, the function will produce the following steps:

1. At index 0, it encounters an opening bracket `(')`, so it pushes the index `0` to the stack.
2. At index 1, it encounters another opening bracket `('(`, so it pushes the index `1` to the stack.
3. At index 2, it encounters another opening bracket `('(`, so it pushes the index `2` to the stack.
4. At index 3, it encounters a closing bracket `')'`. The stack is not empty, so it creates a substring from index `0` (the top of the stack) to index `3`, which is `'(()'`, and adds it to the result array. Then, it pops the index `0` from the stack.
5. At index 4, it encounters a closing bracket `')'`. The stack is not empty, so it creates a substring from index `1` (the top of the stack) to index `4`, which is `')())'`, and adds it to the result