  if (b === 0) {
    return a;
  }
  return greatestCommonDivisor(b, a % b);
} // Note: This function uses recursion to find the GCD. It's not the most efficient way, but it works for small numbers. For larger numbers, you might want to use the Euclidean algorithm with a loop.



