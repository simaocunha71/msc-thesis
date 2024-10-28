  let stack = [];
  for (let c of string) {
    if (c == '[') {
      stack.push(c);
    } else if (c == ']') {
      if (stack.length > 0) {
        stack.pop();
      } else {
        return false;
      }
    }
  }
  return stack.length > 0;
}
// This function uses a stack to keep track of the opening brackets. When it encounters a closing bracket,
// it checks if the stack is not empty. If the stack is not empty, it pops the opening bracket from the stack.
// If the stack is empty, it means there is no matching opening bracket, so it returns false. At the end,
// it checks if the stack is not empty. If it is not empty, it means there are unmatched opening brackets, so it returns true.
// If the stack is empty, it means all brackets are matched, so it returns false.