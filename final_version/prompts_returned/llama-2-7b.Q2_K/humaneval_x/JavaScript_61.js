/* brackets is a string of "(" and ")".
  return true if every opening bracket has a corresponding closing bracket.

  >>> correctBracketing("(")
  false
  >>> correctBracketing("()")
  true
  >>> correctBracketing("(()())")
  true
  >>> correctBracketing(")(()")
  false
  */
const correctBracketing = (brackets) => {
  const hasClosingBracket = brackets.split('').some((value, index, array) =>
    array[index + 1] && array[index + 1][0] === ')' && index < array.length - 2);

  return hasClosingBracket;
};
