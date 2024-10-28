```
function matchParens(lst) {
  let stack = [];
  for (let str of lst) {
    for (let char of str) {
      if (char === '(') {
        stack.push(char);
      } else if (char === ')') {
        if (stack.length === 0) {
          return 'No';
        }
        stack.pop();
      }
    }
  }
  return stack.length === 0 ? 'Yes' : 'No';
}
```

Explanation:
The problem is asking to check if it is possible to concatenate the two strings in some order, that the resulting string will be good. A string S is considered to be good if and only if all parentheses in S are balanced.

We can solve this problem by using a stack. We iterate over the characters in both strings. If we encounter an open parenthesis '(', we push it onto the stack. If we encounter a close parenthesis ')', we check if the stack is empty. If it is, it means there's no matching open parenthesis, so we return 'No'. If the stack is not empty, we pop the open parenthesis from the stack.

After iterating over all characters in both strings, we check if the stack is empty. If it is, it means all parentheses were matched, so we return 'Yes'. If the stack is not empty, it means there are unmatched open parentheses, so we return 'No'.

This solution has a time complexity of O(n), where n is the total number of characters in both strings. It has a space complexity of O(n), where n is the maximum number of open parentheses in both strings.