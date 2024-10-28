  var stack = [];
  for (let c of brackets) {
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
// The above solution uses a stack to keep track of the opening brackets that have not been closed yet. When we encounter a closing bracket, we check if the stack is empty. If it is, it means that there is no corresponding opening bracket and we return false. If the stack is not empty, we pop the opening bracket from the stack. At the end, we check if the stack is empty. If it is, it means that all opening brackets have been properly closed and we return true. If the stack is not empty, it means that there are some opening brackets that have not been closed yet and we return false.