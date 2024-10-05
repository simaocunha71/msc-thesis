```javascript
const correctBracketing = (brackets) => {
  let stack = [];
  for (let bracket of brackets) {
    if (bracket === "<") {
      stack.push("<");
    } else if (bracket === ">") {
      if (stack.length === 0) {
        return false;
      }
      stack.pop();
    }
  }
  return stack.length === 0;
};
```


Explanation:
The function `correctBracketing` takes a string of brackets as input. It uses a stack to keep track of the opening brackets. For each bracket in the string, if it's an opening bracket, it pushes it onto the stack. If it's a closing bracket, it checks if the stack is empty. If the stack is empty, it means there's no corresponding opening bracket, so it returns `false`. If the stack is not empty, it pops the opening bracket from the stack. Finally, it returns whether the stack is empty or not. If the stack is empty, it means every opening bracket has a corresponding closing bracket, so it returns `true`. Otherwise, it returns `false`. 