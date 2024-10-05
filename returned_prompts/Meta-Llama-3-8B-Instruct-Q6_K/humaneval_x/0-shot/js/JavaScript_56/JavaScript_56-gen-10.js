```
const correctBracketing = (brackets) => {
  const stack = [];
  for (const bracket of brackets) {
    if (bracket === "<") {
      stack.push("<");
    } else if (bracket === ">") {
      if (stack.length === 0) return false;
      stack.pop();
    }
  }
  return stack.length === 0;
};
```


Explanation:
The function `correctBracketing` takes a string of brackets as input and returns a boolean indicating whether every opening bracket has a corresponding closing bracket.

We use a stack data structure to keep track of the opening brackets. When we encounter an opening bracket (`"<"`), we push it onto the stack. When we encounter a closing bracket (`">"`), we check if the stack is empty. If it is, it means there is no corresponding opening bracket, so we return `false`. If the stack is not empty, we pop the opening bracket from the stack.

Finally, after iterating through all the brackets, we check if the stack is empty. If it is, it means every opening bracket had a corresponding closing bracket, so we return `true`. If the stack is not empty, it means there were some opening brackets without corresponding closing brackets, so we return `false`.