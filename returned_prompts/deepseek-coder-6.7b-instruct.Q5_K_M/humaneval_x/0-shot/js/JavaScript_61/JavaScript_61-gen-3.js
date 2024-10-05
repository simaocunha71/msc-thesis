  let stack = [];

  for (let i = 0; i < brackets.length; i++) {
    if (brackets[i] === '(') {
      stack.push(brackets[i]);
    } else if (brackets[i] === ')') {
      if (stack.length === 0) {
        return false;
      } else {
        stack.pop();
      }
    }
  }

  return stack.length === 0;
}

console.log(correctBracketing("("));
console.log(correctBracketing("()"));
console.log(correctBracketing("(()())"));
console.log(correctBracketing(")(()"));

```

In this solution, we're using a stack data structure to keep track of the opening brackets that we encounter. We push onto the stack whenever we encounter an opening bracket, and we pop from the stack whenever we encounter a closing bracket. If we encounter a closing bracket but the stack is empty (meaning there's no matching opening bracket), we return false. If the stack is empty at the end of the string, we return true. If the stack isn't empty at the end of the string, that means there were unmatched opening brackets, so we return false.

This solution runs in O(n) time, where n is the length of the string, and uses O(n) space for the stack.

```





















































































































































































