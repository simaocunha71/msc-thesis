```js
const correctBracketing = (brackets) => {
  const stack = [];
  for (let i = 0; i < brackets.length; i++) {
    if (brackets[i] === '<') {
      stack.push('<');
    } else if (brackets[i] === '>') {
      if (stack.length === 0) {
        return false;
      }
      stack.pop();
    }
  }
  return stack.length === 0;
}
```

Explanation:
We use a stack to keep track of opening brackets. For each opening bracket we encounter, we push it onto the stack. For each closing bracket, we check if the stack is empty (which would mean there's no corresponding opening bracket). If it is, we return false. Otherwise, we pop the last opening bracket from the stack. At the end, if the stack is empty, it means all opening brackets have a corresponding closing bracket, so we return true. Otherwise, we return false.