Here is the solution to the problem:

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

Explanation:

The function `isNested` takes a string as input and checks if it contains a valid subsequence of brackets where at least one bracket is nested.

It uses a stack data structure to keep track of the opening brackets. When an opening bracket is encountered, it is pushed onto the stack. When a closing bracket is encountered, the function checks if the stack is empty. If it is, it means there is no matching opening bracket, so the function returns `false`. If the stack is not empty, it pops the opening bracket from the stack.

After iterating through the entire string, the function checks the length of the stack. If the length is greater than 0, it means there are unmatched opening brackets, so the function returns `true`. If the length is 0, it means all brackets were matched, so the function returns `false`.

This solution has a time complexity of O(n), where n is the length of the input string, and a space complexity of O(n) due to the stack data structure.