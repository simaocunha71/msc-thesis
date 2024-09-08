  let stack = [];
  let correct = true;
  for (let i = 0; i < brackets.length; i++) {
    if (brackets[i] == '(') {
      stack.push('(');
    } else if (brackets[i] == ')') {
      if (stack.length == 0) {
        correct = false;
      } else {
        stack.pop();
      }
    }
  }
  return correct && stack.length == 0;
}



