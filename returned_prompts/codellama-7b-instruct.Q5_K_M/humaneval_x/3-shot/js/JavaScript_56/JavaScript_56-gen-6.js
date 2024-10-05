  const stack = [];
  for (let bracket of brackets) {
    if (bracket == '<') {
      stack.push(bracket);
    } else if (bracket == '>') {
      if (stack.length == 0) {
        return false;
      }
      stack.pop();
    }
  }
  return stack.length == 0;
}



