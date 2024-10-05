  let stack = [];

  for (let i = 0; i < string.length; i++) {
    if (string[i] === '[') {
      stack.push(string[i]);
    } else {
      if (stack.length === 0 || stack[stack.length - 1] !== '[') {
        return false;
      }
      stack.pop();
    }
  }

  return stack.length === 0;
}



