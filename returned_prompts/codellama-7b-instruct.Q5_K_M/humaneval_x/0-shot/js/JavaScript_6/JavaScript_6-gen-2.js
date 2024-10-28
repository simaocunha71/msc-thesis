const parseNestedParens = (paren_string) => {
  const stack = [];
  const levels = [];
  for (const char of paren_string) {
    if (char === '(') {
      stack.push(char);
    } else if (char === ')') {
      stack.pop();
      if (stack.length === 0) {
        levels.push(stack.length);
      }
    }
  }
  return levels;
}
