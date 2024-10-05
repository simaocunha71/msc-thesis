  let stack = [];
  for (let c of string) {
    if (c === '[') {
      stack.push(c);
    } else if (c === ']') {
      if (stack.length > 0) {
        stack.pop();
      } else {
        return false;
      }
    }
  }
  return stack.length > 0;
}