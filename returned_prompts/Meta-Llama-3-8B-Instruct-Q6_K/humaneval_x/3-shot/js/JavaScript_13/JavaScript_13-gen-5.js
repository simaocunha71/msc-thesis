  if (b === 0) {
    return a;
  }
  return greatestCommonDivisor(b, a % b);
} // This is an implementation of the Euclidean algorithm for finding the greatest common divisor of two integers. It works by repeatedly replacing (a, b) with (b, a mod b) until b is zero. At that point, a is the greatest common divisor of the original a and b.