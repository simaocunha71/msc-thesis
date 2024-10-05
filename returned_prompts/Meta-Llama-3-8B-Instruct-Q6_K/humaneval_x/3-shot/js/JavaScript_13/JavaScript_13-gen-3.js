  if (b === 0) {
    return a;
  } else {
    return greatestCommonDivisor(b, a % b);
  }
} // This function uses recursion to find the GCD of two numbers. It works by repeatedly replacing the larger number with the remainder of the division of the larger number by the smaller number, until the remainder becomes zero. At that point, the smaller number is the GCD of the original two numbers.