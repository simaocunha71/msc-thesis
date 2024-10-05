You can use a stack data structure to solve this problem. The idea is to push each opening bracket into the stack and pop it when a closing bracket is encountered. If there is a nested bracket, the stack will not be empty when it reaches the end of the string. Here is a possible implementation in JavaScript:

```javascript
const isNested = (string) => {
  const stack = [];
  for (let i = 0; i < string.length; i++) {
    const c = string[i];
    if (c === '[') {
      stack.push(c);
    } else if (c === ']') {
      if (stack.length > 0) {
        stack.pop();
      } else {
        return false;
      }
    }
  }
  return stack.length > 0;
}
```

This function works by iterating over the characters in the input string. If the current character is an opening bracket, it is pushed onto the stack. If the current character is a closing bracket, it is popped from the stack if the stack is not empty. If the stack is empty when a closing bracket is encountered, it means that the brackets are not properly nested and the function returns `false`.

At the end of the function, if the stack is not empty, it means that there are still opening brackets that have not been closed, so the function returns `true`. Otherwise, it returns `false`.