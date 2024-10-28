Here is the solution using a stack data structure:

```javascript
const correctBracketing = (brackets) => {
  const stack = [];
  for (let i = 0; i < brackets.length; i++) {
    if (brackets[i] === "(") {
      stack.push("(");
    } else if (brackets[i] === ")") {
      if (stack.length === 0) {
        return false; // no matching opening bracket
      } else {
        stack.pop();
      }
    }
  }
  return stack.length === 0; // all brackets have been matched
};
```

The function `correctBracketing` takes a string `brackets` as input, which is a sequence of "(" and ")". It returns a boolean indicating whether every opening bracket has a corresponding closing bracket.

Here is how it works:

1. We create an empty stack.
2. We iterate over the input string. For each character:
   - If the character is an opening bracket "(", we push it onto the stack.
   - If the character is a closing bracket ")", we check if the stack is empty. If it is, it means there is no matching opening bracket, so we return false. If the stack is not empty, we pop the opening bracket from the stack.
3. After iterating over the entire string, we check if the stack is empty. If it is, it means all opening brackets have been matched with corresponding closing brackets, so we return true. If the stack is not empty, it means there are unmatched opening brackets, so we return false.