  let stack = [];

  for (let i = 0; i < string.length; i++) {
    if (string[i] == '[') {
      stack.push(true);
    } else {
      stack.pop();
    }
  }

  return stack.length > 0;
}



