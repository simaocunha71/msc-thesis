Here is a possible implementation of the function:
```
const matchParens = (lst) => {
  const str1 = lst[0];
  const str2 = lst[1];
  const stack = [];

  for (let i = 0; i < str1.length; i++) {
    if (str1[i] === '(') {
      stack.push('(');
    } else {
      if (stack.length === 0 || stack.pop() !== '(') {
        return 'No';
      }
    }
  }

  for (let i = 0; i < str2.length; i++) {
    if (str2[i] === '(') {
      stack.push('(');
    } else {
      if (stack.length === 0 || stack.pop() !== '(') {
        return 'No';
      }
    }
  }

  return stack.length === 0 ? 'Yes' : 'No';
};
```
Here's an explanation of how the function works:

1. We first extract the two input strings `str1` and `str2` from the list `lst`.
2. We create an empty stack `stack`.
3. We iterate through `str1` and `str2` simultaneously. For each character, we check if it's an open parenthesis `(` or a close parenthesis `)`.
4. If we encounter an open parenthesis, we push it onto the stack.
5. If we encounter a close parenthesis, we check if the stack is empty or if the top element of the stack is not an open parenthesis. If either condition is true, we return `'No'`, because the parentheses are not balanced.
6. After iterating through both strings, we check if the stack is empty. If it is, we return `'Yes'`, because the parentheses are balanced. Otherwise, we return `'No'`.

This function uses a stack to keep track of the open parentheses, and checks if the close parentheses match the open ones. If there's a mismatch, it returns `'No'`. If the stack is empty after processing both strings, it returns `'Yes'`. Otherwise, it returns `'No'`.