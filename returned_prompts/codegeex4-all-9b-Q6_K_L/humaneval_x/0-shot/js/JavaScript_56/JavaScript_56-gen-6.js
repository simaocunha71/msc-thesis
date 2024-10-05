Here's one way you can solve this problem in JavaScript:

```javascript
const correctBracketing = (brackets) => {
  let stack = [];

  for (let i = 0; i < brackets.length; i++) {
    if (brackets[i] === "<") {
      stack.push("<");
    } else {
      if (stack.length === 0) {
        return false;
      }
      stack.pop();
    }
  }

  return stack.length === 0;
}
```

The algorithm works by iterating over each character in the input string. If the character is "<", it is pushed onto a stack. If the character is ">", it checks the stack. If the stack is empty or the top of the stack is not "<", it returns false. After iterating over all the characters, it checks if the stack is empty. If it is, it returns true, otherwise, it returns false.