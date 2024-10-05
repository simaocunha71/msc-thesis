You can solve this problem by using a stack data structure. The stack will be used to track the opening brackets. Whenever you encounter a closing bracket, you will pop the top element from the stack and check if it matches the closing bracket. If it doesn't match, or if the stack is empty when you encounter a closing bracket, you will return false. If you reach the end of the string and the stack is not empty, you will also return false. Otherwise, you will return true. Here is the code for this solution:

```js
const correctBracketing = (brackets) => {
  const stack = [];
  for (let i = 0; i < brackets.length; i++) {
    if (brackets[i] === "<") {
      stack.push("<");
    } else if (brackets[i] === ">") {
      if (stack.length === 0) {
        return false;
      } else {
        stack.pop();
      }
    }
  }
  return stack.length === 0;
}
```

This solution has a time complexity of O(n), where n is the length of the input string.