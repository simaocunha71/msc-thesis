function isNested(string) {

  let stack = [];

  for (let char of string) {
    if (char === '[' && !stack.length) {
      stack.push(char);
    } else if (char === ']' && !stack.length) {
      return false;
    } else if (char === ']') {
      if (stack[stack.length - 1] === '[') {
        stack.pop();
      } else {
        stack.push(char);
      }
    } else {
      stack.push(char);
    }
  }

  return !stack.length;
}