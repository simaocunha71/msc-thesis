/* Create a function that takes 3 numbers.
  Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
  Returns false in any other cases.
  Examples
  anyInt(5, 2, 7) ➞ true
  anyInt(3, 2, 2) ➞ false
  anyInt(3, -2, 1) ➞ true
  anyInt(3.6, -2.2, 2) ➞ false
  */
const anyInt = (x, y, z) => {
  if ((z === x + y) && isFiniteNumber(parseInt(y)) && isFiniteNumber(parseInt(x))) return true;
  if (!(z === x + y) || !isFiniteNumber(parseInt(y)) || !isFiniteNumber(parseInt(x))) return false;
};
function isFiniteNumber(num) {
  return parseInt(num) % 1 === 0 && !!isNaN(parseFloat(num));
}
