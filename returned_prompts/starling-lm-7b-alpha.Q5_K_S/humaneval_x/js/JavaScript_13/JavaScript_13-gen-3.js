  if (b == 0) {
    return a;
  } else {
    return greatestCommonDivisor(b, a % b);
  }
}


