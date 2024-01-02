/* Return a greatest common divisor of two integers a and b
  >>> greatestCommonDivisor(3, 5)
  1
  >>> greatestCommonDivisor(25, 15)
  5
  */
const greatestCommonDivisor = (a, b) => {
  if (!b || !a) return a;

  const divider = Math.min(Math.floorModulo(a, b), Math.floorModulo(b, a));
  return (divider === 0 ? Infinity : divider);
};
