  let result = 1;
  let base = n % p;
  while (p > 0) {
    if (p % 2 == 1) {
      result = (result * base) % p;
    }
    p = Math.floor(p / 2);
    base = (base * base) % p;
  }

  return result;
}