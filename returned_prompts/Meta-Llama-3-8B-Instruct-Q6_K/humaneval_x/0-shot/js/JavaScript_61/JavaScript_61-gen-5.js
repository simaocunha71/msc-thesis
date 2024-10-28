Here is the solution using a stack data structure:
```
const correctBracketing = (brackets) => {
  const stack = [];
  for (const bracket of brackets) {
    if (bracket === "(") {
      stack.push(bracket);
    } else if (bracket === ")") {
      if (stack.length === 0 || stack.pop() !== "(") {
        return false;
      }
    }
  }
  return stack.length === 0;
};
```
Here's an explanation of how the code works:

1. We create an empty stack `[]`.
2. We iterate over the input string `brackets`.
3. For each character, we check if it's an opening bracket `(` or a closing bracket `)`.
4. If it's an opening bracket, we push it onto the stack.
5. If it's a closing bracket, we check if the stack is empty or if the top element of the stack is not an opening bracket `(`. If either of these conditions is true, we return `false`, because there's no corresponding opening bracket.
6. If the stack is empty after iterating over the entire string, we return `true`, because every opening bracket had a corresponding closing bracket.

This solution has a time complexity of O(n), where n is the length of the input string, and a space complexity of O(n) for the stack.