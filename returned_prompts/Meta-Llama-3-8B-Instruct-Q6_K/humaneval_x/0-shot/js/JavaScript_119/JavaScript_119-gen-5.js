Here is the solution using a stack data structure:
```
const matchParens = (lst) => {
  const stack = [];
  for (const s of lst) {
    for (const c of s) {
      if (c === '(') {
        stack.push(c);
      } else if (c === ')') {
        if (stack.length === 0) {
          return 'No';
        }
        stack.pop();
      }
    }
  }
  return stack.length === 0 ? 'Yes' : 'No';
};
```
Here's an explanation of the code:

1. We initialize an empty stack `stack`.
2. We iterate through each string in the input list `lst`.
3. For each string, we iterate through each character `c`.
4. If `c`