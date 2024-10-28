```js
const correctBracketing = (brackets) => {
  const stack = [];
  for (let i = 0; i < brackets.length; i++) {
    const char = brackets[i];
    if (char === '(') {
      stack.push(char);
    } else if (char === ')') {
      if (stack.length === 0) {
        return false;
      } else {
        stack.pop();
      }
    }
  }
  return stack.length === 0;
}
```