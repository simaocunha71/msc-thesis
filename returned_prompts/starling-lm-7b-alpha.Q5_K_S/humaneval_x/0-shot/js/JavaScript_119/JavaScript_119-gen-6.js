To determine if a string of parentheses is balanced, we can use a stack.
Here's how:

1. Initialize an empty stack.
2. Iterate through each character of the string.
3. If the character is an open parentheses '(', push it onto the stack.
4. If the character is a close parentheses ')', pop the stack and make sure there was an open parentheses
   that was pushed onto the stack previously. If there wasn't, this is an unbalanced string, so we return false.
5. After checking all the characters in the string, we check the stack. If the stack is empty, this means all
   the open parentheses were matched with close parentheses. If not, this is an unbalanced string.
6. If the stack is empty, return true, otherwise return false.

To solve the problem, we can iterate through each string in the list, and check if they are balanced individually. If any string in the list is not balanced, we can immediately return no. If all strings are balanced, we can concatenate them and check if the resulting string is balanced. If it is, we return yes, otherwise we return no.

Here's the code to solve the problem:

```
const matchParens = (lst) => {
  for (const str of lst) {
    if (!isBalanced(str)) {
      return "No";
    }
  }

  const concatStr = lst.join("");
  return isBalanced(concatStr) ? "Yes" : "No";
};

const isBalanced = (str) => {
  let stack = [];
  for (const char of str) {
    if (char === "(") {
      stack.push(char);
    } else if (char === ")") {
      if (stack.length === 0) {
        return false;
      } else {
        stack.pop();
      }
    }
  }
  return stack.length === 0;
};
```

The time complexity of this solution is O(n), where n is the total number of characters in all the strings in the list. The space complexity is O(n) as well, as we