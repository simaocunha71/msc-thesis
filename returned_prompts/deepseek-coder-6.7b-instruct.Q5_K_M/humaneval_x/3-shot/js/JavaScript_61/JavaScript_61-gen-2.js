  var stack = [];

  for  (let i = 0; i < brackets.length; i++) {
    if (brackets[i] === '(') {
      stack.push('(');
    } else if (brackets[i] === ')') {
      if (!stack.length) {
        return false;
      }
      stack.pop();
    }
  }

  return stack.length === 0;
}



