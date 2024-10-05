const correctBracketing = (brackets) => {
  let bracketCount = 0;
  for (let i = 0; i < brackets.length; i++) {
    if (brackets[i] === "(") {
      bracketCount++;
    } else {
      bracketCount--;
    }
    if (bracketCount < 0) {
      return false;
    }
  }
  return bracketCount === 0;
}

console.log(correctBracketing("(")); // false
console.log(correctBracketing("()")); // true
console.log(correctBracketing("(()())")); // true
console.log(correctBracketing(")(()")); // false