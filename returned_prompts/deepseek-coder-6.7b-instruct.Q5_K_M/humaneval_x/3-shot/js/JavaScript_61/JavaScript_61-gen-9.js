  var stack = [];

  for (const bracket of brackets) {
    if (bracket === "(") {
      stack.push(bracket);
    } else if (bracket === ")") {
      if (!stack.length) {
        return false;
      }
      stack.pop();
    }
  }

  return !stack.length;
}



