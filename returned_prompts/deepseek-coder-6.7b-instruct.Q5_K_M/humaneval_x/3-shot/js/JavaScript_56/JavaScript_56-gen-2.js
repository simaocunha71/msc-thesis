  let stack = [];
  for (let i = 0; i < brackets.length; i++) {
    if (brackets[i] === "<") {
      stack.push("<");
    } else if (stack.length === 0) {
      return false;
    } else {
      stack.pop();
    }
  }
  return stack.length === 0;
}



