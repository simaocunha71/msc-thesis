const greatestCommonDivisor = (a, b) => {
  if (a < 0 || b < 0) {
    throw new Error('Input must be non-negative integers');
  }
  if (a === 0) {
    return b;
  }
  if (b === 0) {
    return a;
  }
  if (a === b) {
    return a;
  }
  if (a > b) {
    return greatestCommonDivisor(a - b, b);
  } else {
    return greatestCommonDivisor(a, b - a);
  }
}

console.log(greatestCommonDivisor(3, 5)); // 1
console.log(greatestCommonDivisor(25, 15)); // 5
console.log(greatestCommonDivisor(0, 5)); // 5
console.log(greatestCommonDivisor(5, 0)); // 5
console.log(greatestCommonDivisor(5, 5)); // 5
console.log(greatestCommonDivisor(10, 15)); // 5
console.log(greatestCommonDivisor(15, 10)); // 5
console.log(greatestCommonDivisor(0, 0)); // 0
console.log(greatestCommonDivisor(1, 0)); // 1
console.log(greatestCommonDivisor(0, 1)); // 1