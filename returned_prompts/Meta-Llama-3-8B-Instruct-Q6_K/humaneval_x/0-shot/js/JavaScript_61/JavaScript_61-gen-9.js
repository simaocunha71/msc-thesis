Here is a simple solution that uses a stack to keep track of the opening brackets:

```javascript
const correctBracketing = (brackets) => {
  const stack = [];
  for (let i = 0; i < brackets.length; i++) {
    if (brackets[i] === "(") {
      stack.push("(");
    } else if (brackets[i] === ")") {
      if (stack.length === 0) {
        return false;
      }
      stack.pop();
    }
  }
  return stack.length === 0;
};
```

This function iterates over the input string, pushing opening brackets onto the stack and popping them off when it encounters a closing bracket. If it encounters a closing bracket when the stack is empty, it returns false. After iterating over the entire string, it returns true if the stack is empty (i.e., all opening brackets had corresponding closing brackets) and false otherwise.