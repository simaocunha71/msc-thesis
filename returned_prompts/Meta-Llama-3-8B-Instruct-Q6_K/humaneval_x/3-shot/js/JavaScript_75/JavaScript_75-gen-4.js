  for (let i = 2; i < 100; i++) {
    if (isPrime(i) && a % i == 0) {
      for (let j = i; j < 100; j++) {
        if (isPrime(j) && a % j == 0) {
          for (let k = j; k < 100; k++) {
            if (isPrime(k) && a % k == 0) {
              return true;
            }
          }
        }
      }
    }
  }
  return false;

  function isPrime(n) {
    for (let i = 2; i <= Math.sqrt(n); i++) {
      if (n % i == 0) {
        return false;
      }
    }
    return true;
  }
}