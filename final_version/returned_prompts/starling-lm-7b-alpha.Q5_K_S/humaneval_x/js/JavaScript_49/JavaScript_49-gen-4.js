  let result = 1;

  while (n > 0) {
    if (n % 2 == 1) {
      result = (result * Math.floor(p)) % p;
    }
    n >>= 1;
    p = (p * Math.floor(p)) % p;
  }

  return result;
}



