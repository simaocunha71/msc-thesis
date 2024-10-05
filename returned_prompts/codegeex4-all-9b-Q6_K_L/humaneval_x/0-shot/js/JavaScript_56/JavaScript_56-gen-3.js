```js
const correctBracketing = (brackets) => {
  let stack = [];
  let bracketMap = {
    "<": ">",
    ">": "<"
  };
  for (let i = 0; i < brackets.length; i++) {
    if (brackets[i] === "<") {
      stack.push("<");
    } else {
      if (stack.length === 0) {
        return false;
      } else {
        if (bracketMap[stack.pop()] !== brackets[i]) {
          return false;
        }
      }
    }
  }
  return stack.length === 0;
}
```