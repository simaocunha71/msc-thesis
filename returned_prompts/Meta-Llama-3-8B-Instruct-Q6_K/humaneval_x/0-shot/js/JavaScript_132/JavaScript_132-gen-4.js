Here is a simple function that solves the problem:

```javascript
const isNested = (string) => {
  let stack = [];
  for (let char of string) {
    if (char === '[') {
      stack.push(char);
    } else if (char === ']') {
      if (stack.length === 0) return false;
      stack.pop();
    }
  }
  return stack.length > 0;
};
```

The function uses a stack to keep track of the opening brackets. It iterates over the string, and for each opening bracket, it pushes it onto the stack. For each closing bracket, it checks if the stack is empty (which would mean there's no matching opening bracket). If the stack is not empty, it pops the opening bracket from the stack. At the end of the iteration, the function checks if the stack is not empty. If it's not empty, it means there's an opening bracket that doesn't have a matching closing bracket, so the function returns true. If the stack is empty, it means all brackets were matched correctly, so the function returns false.