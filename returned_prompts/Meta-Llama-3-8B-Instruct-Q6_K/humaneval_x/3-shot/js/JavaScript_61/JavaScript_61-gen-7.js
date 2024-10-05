  var stack = [];
  for (const c of brackets) {
    if (c == '(') {
      stack.push(c);
    } else if (c == ')') {
      if (stack.length == 0) {
        return false;
      }
      stack.pop();
    }
  }
  return stack.length == 0;
}
// This solution uses a stack to keep track of the opening brackets. When a closing bracket is encountered, it checks if there are any opening brackets in the stack. If not, it returns false. If the stack is empty at the end, it means all opening brackets had corresponding closing brackets.