  let result = 1;
  while (n > 0) {
    if (n % 2 == 1) {
      result *= p;
      result %= p;
    }
    p *= p;
    p %= p;
    n >>= 1;
  }
  return result;
}



