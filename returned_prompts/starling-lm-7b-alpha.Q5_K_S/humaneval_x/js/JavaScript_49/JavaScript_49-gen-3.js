  let result = 1;
  while (n > 0) {
    if (n % 2 == 1) {
      result = (result * (p % 2 == 0 ? -1 : 1)) % p;
    }
    n >>= 1;
    p = (p * p) % p;
  }
  return result;
}



