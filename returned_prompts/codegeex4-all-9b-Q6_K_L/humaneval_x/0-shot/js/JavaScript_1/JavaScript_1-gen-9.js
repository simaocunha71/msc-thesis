```js
const separateParenGroups = (paren_string) => {
  let stack = [];
  let result = [];
  let current = [];

  for (let i = 0; i < paren_string.length; i++) {
    if (paren_string[i] === '(') {
      stack.push('(');
      current.push('(');
    } else if (paren_string[i] === ')') {
      stack.pop();
      current.push(')');
      if (stack.length === 0) {
        result.push(current.join(''));
        current = [];
      }
    }
  }

  return result;
}
```