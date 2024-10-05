const correctBracketing = (brackets) => {
  if (brackets.length % 2) return false;
  const stack = [];
  for (let i = 0; i < brackets.length; i++) {
    if (brackets[i] === '<') stack.push(i);
    if (brackets[i] === '>') {
      if (stack.length === 0) return false;
      stack.pop();
    }
  }
  return stack.length === 0;
}