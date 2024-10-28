  for (let i = 2; i <= 100; i++) {
    for (let j = i + 1; j <= 100; j++) {
      for (let k = j + 1; k <= 100; k++) {
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
    for (let i = 2; i * i <= n; i++) {
      if (n % i === 0) {
        return false;
      }
    }
    return true;
  }
}