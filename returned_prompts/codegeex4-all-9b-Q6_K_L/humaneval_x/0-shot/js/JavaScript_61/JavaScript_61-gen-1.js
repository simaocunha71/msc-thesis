Here is the solution in JavaScript:

```javascript
const correctBracketing = (brackets) => {
  let stack = [];
  for(let i = 0; i < brackets.length; i++) {
    if(brackets[i] === '(') {
      stack.push('(');
    } else if(brackets[i] === ')') {
      if(stack.length === 0) {
        return false;
      }
      stack.pop();
    }
  }
  return stack.length === 0;
}
```

Explanation:
- We use a stack to keep track of the opening brackets.
- For each bracket in the string, if it's an opening bracket, we push it onto the stack.
- If it's a closing bracket, we check if the stack is empty. If it is, it means we have a closing bracket without a corresponding opening bracket, so we return false.
- If the stack is not empty, we pop the top element from the stack.
- After checking all the brackets, if the stack is empty, it means we have found a corresponding closing bracket for every opening bracket, so we return true. Otherwise, we return false.