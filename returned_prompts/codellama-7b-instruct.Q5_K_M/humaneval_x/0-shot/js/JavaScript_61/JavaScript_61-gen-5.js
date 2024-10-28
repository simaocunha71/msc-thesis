const correctBracketing = (brackets) => {
  return brackets.split("").reduce((acc, curr) => {
    if (curr === "(") {
      acc++;
    } else if (curr === ")") {
      acc--;
    }
    return acc;
  }, 0) === 0;
};

B:
const correctBracketing = (brackets) => {
  const stack = [];
  for (let i = 0; i < brackets.length; i++) {
    if (brackets[i] === "(") {
      stack.push(i);
    } else if (brackets[i] === ")") {
      stack.pop();
    }
  }
  return stack.length === 0;
};