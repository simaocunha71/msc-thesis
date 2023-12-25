/* Return a greatest common divisor of two integers a and b
  >>> greatestCommonDivisor(3, 5)
  1
  >>> greatestCommonDivisor(25, 15)
  5
  */
const greatestCommonDivisor = (a, b) => {
  if (b === 0) return a;
  while (--b >= 0 && a % b !== 0);
  return a == 0 ? 1 : --b;
};

/*
  >>> greatestCommonFactor(3, 5)
  1
*/
const greatestCommonDivisor = (a, b) => {
  if (!a || !b) throw new Error('Invalid parameters!');
  return Math.gcd(a, b);
};
