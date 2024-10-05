```javascript
const isNested = (string) => {
  const stack = [];
  for (let i = 0; i < string.length; i++) {
    if (string[i] === '[') {
      stack.push(i);
    } else {
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
