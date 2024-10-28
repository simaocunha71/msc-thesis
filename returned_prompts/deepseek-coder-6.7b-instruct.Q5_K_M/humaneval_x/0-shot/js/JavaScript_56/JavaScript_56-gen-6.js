  const stack = [];

  for(let i = 0; i < brackets.length; i++) {
    if(brackets[i] === "<") {
      stack.push("<");
    } else if(brackets[i] === ">") {
      if(stack.length === 0) {
        return false;
      } else {
        stack.pop();
      }
    }
  }

  return stack.length === 0;
}


console.log(correctBracketing("<"));  // false
console.log(correctBracketing("<>"));  // false
console.log(correctBracketing("<<><>>"));  // false
console.log(correctBracketing("><<>"));  // false
console.log(correctBracketing("<<>>"));  // true
console.log(correctBracketing("<<><>>"));  // true






```

The solution uses the concept of a stack. A stack is a linear data structure that follows the Last-In-First-Out (LIFO) principle. In this problem, we use a stack to check if each opening bracket has a corresponding closing bracket. We push every opening bracket into the stack and pop the last element of the stack when we encounter a closing bracket. If the stack is not empty after traversing all brackets, it means there exists an opening bracket without a corresponding closing bracket, hence we return false. Otherwise, we return true.

The time complexity of this solution is O(n), where n is the length of the input string. The space complexity is also O(n) due to the use of the stack to store all the brackets.
```

## Task 4

```javascript
