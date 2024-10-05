const correctBracketing = (brackets) => {
  const closingBrackets = ")]}";

  let stack = [];

  for (let char of brackets) {
    if (closingBrackets.includes(char)) {
      if (stack.pop() !== char) {
        return false;
      }
    } else {
      stack.push(char);
    }
  }

  return stack.length === 0;
}
