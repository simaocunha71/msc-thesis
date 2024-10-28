const correctBracketing = (brackets) => {
  let openBrackets = 0;
  for (let i = 0; i < brackets.length; i++) {
    if (brackets[i] === "<") {
      openBrackets++;
    } else if (brackets[i] === ">") {
      openBrackets--;
    }
    if (openBrackets < 0) {
      return false;
    }
  }
  return openBrackets === 0;
}