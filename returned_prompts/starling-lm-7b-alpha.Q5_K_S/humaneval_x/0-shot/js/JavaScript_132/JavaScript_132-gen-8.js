To determine if a string contains at least one nested sequence of square brackets, we can use a stack to keep track of the opening brackets we encounter. Here's how we can do it:

1. Create an empty stack.
2. Iterate through each character of the input string.
3. If the character is an opening bracket, push it onto the stack.
4. If the character is a closing bracket, pop the last element from the stack and check if the popped element is the same as the current bracket. If they are not the same, return false. If they are the same, continue with the next character.
5. After iterating through all the characters, if the stack is not empty, return false. Otherwise, return true.

Here's a step-by-step breakdown of the solution:

1. We start with an empty stack.
2. We iterate through each character of the input string.
3. For each opening bracket we encounter, we push it onto the stack.
4. For each closing bracket we encounter, we pop the last element from the stack and check if the popped element is the same as the current bracket. If they are not the same, it means there is no nested sequence of brackets, so we return false. If they are the same, we continue with the next character.
5. After iterating through all the characters, if the stack is not empty, it means there is no nested sequence of brackets, so we return false. Otherwise, we return true.

Here's how the solution looks in JavaScript:

```javascript
const isNested = (string) => {
  const stack = [];

  for (let char of string) {
    if (char === '[') {
      stack.push(char);
    } else if (char === ']') {
      if (stack.length === 0 || stack.pop() !== '[') {
        return false;
      }
    }
  }

  return stack.length === 0;
};
```

And here are some test cases to verify the solution:

```javascript
console.log(isNested('[[]]'));       // true
console.log(isNested('[]]]]]]][[[[[]