  let stack = [];
  for (const bracket of brackets) {
    if (bracket === '<') {
      stack.push(bracket);
    } else if (bracket === '>' && stack.length > 0) {
      stack.pop();
    } else {
      return false;
    }
  }
  return stack.length === 0;
}



