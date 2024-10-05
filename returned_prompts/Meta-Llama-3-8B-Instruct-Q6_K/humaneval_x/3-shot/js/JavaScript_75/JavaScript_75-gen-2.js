  for (let i = 2; i <= 100; i++) {
    for (let j = i; j <= 100; j++) {
      for (let k = j; k <= 100; k++) {
        if (i * j * k === a) {
          if (isPrime(i) && isPrime(j) && isPrime(k)) {
            return true;
          }
        }
      }
    }
  }
  return false;

  function isPrime(n) {
    if (n <= 1) {
      return false;
    }
    for (let i = 2; i * i <= n; i++) {
      if (n % i === 0) {
        return false;
      }
    }
    return true;
  }
}