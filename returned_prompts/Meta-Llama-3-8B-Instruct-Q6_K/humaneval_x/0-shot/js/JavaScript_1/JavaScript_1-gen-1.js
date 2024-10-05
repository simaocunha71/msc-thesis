Here is the solution using a stack:

```javascript
const separateParenGroups = (paren_string) => {
  const stack = [];
  const result = [];
  let currentParen = '';

  for (let char of paren_string) {
    if (char === '(') {
      stack.push(char);
      currentParen += char;
    } else if (char === ')') {
      if (stack.length > 0) {
        stack.pop();
        currentParen += char;
        if (stack.length === 0) {
          result.push(currentParen);
          currentParen = '';
        }
      } else {
        return []; // Unbalanced parentheses
      }
    }
  }

  if (stack.length > 0) {
    return []; // Unbalanced parentheses
  }

  return result;
};

console.log(separateParenGroups('( ) (( )) (( )( ))'));
// Output: ["()", "(())", "(()())"]
```

In this solution, we iterate over the input string and use a stack to keep track of the opening parentheses. When we encounter a closing parenthesis, we pop the corresponding opening parenthesis from the stack and add it to the current string. If the stack is empty when we encounter a closing parenthesis, it means we have an unbalanced group of parentheses, so we return an empty array. If the stack is not empty at the end of the iteration, it means there are unmatched opening parentheses, so we also return an empty array. Otherwise, we add the current string to the result array and reset it for the next group of parentheses. Finally, we return the result array.