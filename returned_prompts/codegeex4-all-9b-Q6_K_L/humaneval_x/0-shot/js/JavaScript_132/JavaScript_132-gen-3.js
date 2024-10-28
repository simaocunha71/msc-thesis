```js
const isNested = (string) => {
  let stack = [];
  for (let i = 0; i < string.length; i++) {
    if (string[i] === '[') {
      stack.push(string[i]);
    } else if (string[i] === ']') {
      if (stack.length > 0 && stack[stack.length - 1] === '[') {
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
