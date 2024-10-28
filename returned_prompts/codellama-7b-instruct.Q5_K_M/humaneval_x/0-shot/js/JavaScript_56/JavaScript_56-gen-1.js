/* brackets is a string of "<" and ">".
  return false if every opening bracket has a corresponding closing bracket.

  >>> correctBracketing("<")
  false
  >>> correctBracketing("<>")
  false
  >>> correctBracketing("<<><>>")
  false
  >>> correctBracketing("><<>")
  false
  */
const correctBracketing = (brackets) => {
  let stack = [];
  for (let i=0; i<brackets.length; i++) {
    if (brackets[i] === "<") {
      stack.push("<");
    } else if (brackets[i] === ">") {
      let last = stack.pop();
      if (last !== "<") {
        return false;
      }
    }
  }
  return stack.length === 0;
}

B:
/* brackets is a string of "<" and ">".
  return false if every opening bracket has a corresponding closing bracket.

  >>> correctBracketing("<")
  false
  >>> correctBracketing("<>")
  false
  >>> correctBracketing("<<><>>")
  false
  >>> correctBracketing("><<>")
  false
  */
const correctBracketing = (brackets) => {
  let stack = [];
  for (let i=0; i<brackets.length; i++) {
    if (brackets[i] === "<") {
      stack.push("<");
    } else if (brackets[i] === ">") {
      if (stack.pop() !== "<") {
        return false;
      }
    }
  }
  return stack.length === 0;
}

C:
/* brackets is a string of "<" and ">".
  return false if every opening bracket has a corresponding closing bracket.

  >>> correctBracketing("<")
  false
  >>> correctBracketing("<>")
  false
  >>> correctBracketing("<<><>>")
  false
  >>> correctBracketing("><<>")
  false
  */
const correctBracketing = (brackets) => {
