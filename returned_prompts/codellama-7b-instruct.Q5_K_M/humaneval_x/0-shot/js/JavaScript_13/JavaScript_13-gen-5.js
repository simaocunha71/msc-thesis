/* Return a greatest common divisor of two integers a and b
  >>> greatestCommonDivisor(3, 5)
  1
  >>> greatestCommonDivisor(25, 15)
  5
  */
const greatestCommonDivisor = (a, b) => {
  if (a === b) {
    return a;
  } else if (a < b) {
    return greatestCommonDivisor(b % a, a);
  } else {
    return greatestCommonDivisor(b % a, a);
  }
};

