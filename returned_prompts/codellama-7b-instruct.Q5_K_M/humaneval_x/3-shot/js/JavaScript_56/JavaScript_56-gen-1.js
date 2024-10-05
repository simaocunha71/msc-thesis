  let stack = [];
  for (const bracket of brackets) {
    if (bracket == '<') {
      stack.push(bracket);
    } else if (stack.length == 0) {
      return false;
    } else {
      stack.pop();
    }
  }
  return stack.length == 0;
}



