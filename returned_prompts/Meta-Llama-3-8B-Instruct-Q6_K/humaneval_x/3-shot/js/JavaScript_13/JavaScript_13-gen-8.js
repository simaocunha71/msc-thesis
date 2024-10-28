  if (b === 0) {
    return a;
  } else {
    return greatestCommonDivisor(b, a % b);
  }
} // This function is recursive and will continue to call itself until b is 0. At that point, a is the GCD.