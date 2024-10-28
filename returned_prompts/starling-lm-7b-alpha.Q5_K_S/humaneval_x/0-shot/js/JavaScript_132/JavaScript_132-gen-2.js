To solve this problem, we can follow these steps:

1. Initialize a stack with a capacity equal to the length of the input string.
2. Iterate through the string from left to right.
3. If the current character is an opening bracket ('['), push it onto the stack.
4. If the current character is a closing bracket (']'), check if the stack is empty.
5. If the stack is empty, return false as there are no opening brackets to match the closing brackets.
6. If the stack is not empty, pop an opening bracket from the stack.
7. If there are no opening brackets to match the closing brackets, or if there are opening brackets but none of them is nested, return false.
8. If the stack is empty after processing all characters in the string, return true as there is at least one bracket that is nested.

Here's the code that implements the above steps:

```javascript
const isNested = (string) => {
  const stack = [];

  for (let i = 0; i < string.length; i++) {
    if (string[i] === '[') {
      stack.push(i);
    } else if (string[i] === ']') {
      if (stack.length === 0) {
        return false;
      }
      stack.pop();
    }
  }

  return stack.length > 0;
};
```

The `isNested` function takes a string as input and initializes an empty stack. It then iterates through the string, pushing opening brackets onto the stack and popping closing brackets from the stack. If there are no opening brackets to match the closing brackets, the function returns false. If there are opening brackets but none of them are nested, the function also returns false. If there is at least one bracket that is nested, the function returns true.

To test the function, you can use the following test cases:

```javascript
console.log(isNested('[[]]'));      // true
console.log(isNested('[]]]]]]][[[[[]'));  // false
console.log(isNested('[][]