  if (a == b) return a;
  if (a < b) return greatestCommonDivisor(b, a);
  if (a % b == 0) return b;
  return greatestCommonDivisor(a % b, b);
}



