```javascript
const isNested = (string) => {
  let stack = [];
  for (let char of string) {
    if (char === '[') {
      stack.push(char);
    } else if (char === ']') {
      if (stack.length > 0) {
        stack.pop();
        if (stack.length > 0) {
          return true;
        }
      }
    }
  }
  return false;
}
```