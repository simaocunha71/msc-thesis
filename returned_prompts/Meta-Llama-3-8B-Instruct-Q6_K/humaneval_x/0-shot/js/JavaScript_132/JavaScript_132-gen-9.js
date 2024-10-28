Here is the solution:
```javascript
const isNested = (string) => {
  let stack = [];
  for (let char of string) {
    if (char === '[') {
      stack.push(char);
    } else if (char === ']') {
      if (stack.length > 0) {
        stack.pop();
      } else {
        return false;
      }
    }
  }
  return stack.length > 0;
};
```
Here's an explanation of the code:

* We create an empty stack `stack` to keep track of the opening brackets.
* We iterate through each character in the input string.
* If we encounter an opening bracket `[]`, we push it onto the stack.
* If we encounter a closing bracket `]`, we check if the stack is empty. If it is, it means there's no matching opening bracket, so we return `false`. If the stack is not empty, we pop the opening bracket from the stack.
* After iterating through the entire string, we check if the stack is empty or not. If it's not empty, it means there was at least one nested bracket, so we return `true`. If it's empty, it means all brackets were matched and there was no nesting, so we return `false`.

You can test this function with the examples you provided to see that it returns the correct results.