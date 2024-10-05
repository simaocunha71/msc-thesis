  if (a == 0) {
    return b;
  } else if (b == 0) {
    return a;
  } else {
    return greatestCommonDivisor(b % a, a);
  }
}



