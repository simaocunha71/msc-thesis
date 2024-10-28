  const isPrime = (n) => {
    if (n <= 1) {
      return false;
    }
    for (let i = 2; i <= Math.sqrt(n); i++) {
      if (n % i == 0) {
        return false;
      }
    }
    return true;
  };

  let count = 0;
  for (let i = 2; i <= Math.sqrt(a); i++) {
    if (a % i == 0 && isPrime(i)) {
      count += 1;
    }
  }

  return count == 3;
}