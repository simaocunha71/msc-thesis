  const primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97];
  if (a < 2) {
    return false;
  }
  for (const prime of primes) {
    if (a % prime == 0) {
      a /= prime;
      if (a == 1) {
        return true;
      }
    }
  }
  return false;
}

