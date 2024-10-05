const correctBracketing = (brackets) => {
  let balance = 0;
  for (let i = 0; i < brackets.length; i++) {
    if (brackets[i] === "<") {
      balance++;
    } else {
      balance--;
    }
    if (balance < 0) {
      return false;
    }
  }
  return balance === 0;
}