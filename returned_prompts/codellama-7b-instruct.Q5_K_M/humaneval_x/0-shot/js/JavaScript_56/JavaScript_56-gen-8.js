const correctBracketing = (brackets) => {
  const stack = [];
  const closingBrackets = {
    ">": "<",
    ")": "(",
    "]": "[",
  };
  for (let char of brackets) {
    if (closingBrackets[char]) stack.push(closingBrackets[char]);
    else if (stack.pop() !== char) return false;
  }
  return stack.length === 0;
}

