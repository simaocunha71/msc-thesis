  let balance = 0;

  for (const bracket of brackets) {
    if (bracket == '(') {
      balance += 1;
    } else if (bracket == ')') {
      balance -= 1;
    }
    if (balance < 0) {
      return false;
    }
  }
  return balance == 0;
}
// another solution
const correctBracketing = (brackets) => {
  let stack = [];
  for (const bracket of brackets) {
    if (bracket == '(') {
      stack.push(bracket);
    } else if (bracket == ')') {
      if (stack.length == 0) {
        return false;
      }
      stack.pop();
    }
  }
  return stack.length == 0;
}