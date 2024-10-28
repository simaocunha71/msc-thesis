  if (a === 0 || b === 0) {
    return 0;
  }
  if (a === b) {
    return a;
  }
  if (a < b) {
    return greatestCommonDivisor(b, a);
  }
  return greatestCommonDivisor(a % b, b);
}



