  if (b === 0) {
    return a;
  }
  return greatestCommonDivisor(b, a % b);
}
// or
const greatestCommonDivisor = (a, b) => {
  while (b !== 0) {
    let temp = b;
    b = a % b;
    a = temp;
  }
  return a;
}
// or
const greatestCommonDivisor = (a, b) => {
  if (b === 0) {
    return a;
  }
  return Math.abs(Math.gcd(a % b, b));
}
// gcd function
Math.gcd = function(a, b) {
  if (b === 0) {
    return a;
  }
  return Math.gcd(b, a % b);
};