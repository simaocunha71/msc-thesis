const greatestCommonDivisor = (a, b) => {
  if (b === 0) {
    return a;
  }
  return greatestCommonDivisor(b, a % b);
};

console.log(greatestCommonDivisor(3, 5)); // 1
console.log(greatestCommonDivisor(25, 15)); // 5

This algorithm is based on the Euclidean algorithm for finding the greatest common divisor of two integers. It repeatedly replaces the larger number with the remainder of the two numbers until the remainder is zero. At that point, the other number is the greatest common divisor.