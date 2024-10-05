```javascript
const correctBracketing = (brackets) => {
  const stack = [];
  for (let i = 0; i < brackets.length; i++) {
    if (brackets[i] === "(") {
      stack.push("(");
    } else if (brackets[i] === ")") {
      if (stack.length === 0) {
        return false;
      } else {
        stack.pop();
      }
    }
  }
  return stack.length === 0;
};
```


Explanation:
The function `correctBracketing` takes a string `brackets` as input and returns `true` if every opening bracket has a corresponding closing bracket, and `false` otherwise.

The function uses a stack data structure to keep track of the opening brackets. It iterates over the input string, and for each character:

- If the character is an opening bracket `(`, it pushes it onto the stack.
- If the character is a closing bracket `)`, it checks if the stack is empty. If it is, it means there's no corresponding opening bracket, so it returns `false`. If the stack is not empty, it pops the opening bracket from the stack.

After iterating over the entire string, the function checks if the stack is empty. If it is, it means every opening bracket had a corresponding closing bracket, so it returns `true`. If the stack is not empty, it means there were opening brackets without corresponding closing brackets, so it returns `false`.