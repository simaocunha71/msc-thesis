
const correctBracketing = (brackets) => {
  let stack = [];
  let counter = 0;
  const open = ["(", "{", "["];
  const close = [")", "}", "]"];
  for (let char of brackets) {
    if (open.includes(char)) {
      stack.push(char);
    }
    if (close.includes(char)) {
      if (stack.length === 0) {
        return false;
      }
      if (open.indexOf(stack.pop()) !== close.indexOf(char)) {
        return false;
      }
    }
  }
  return stack.length === 0;
}