  if (a < b) {
    return greatestCommonDivisor(b, a);
  }
  if (b == 0) {
    return a;
  }
  return greatestCommonDivisor(b, a % b);
}



