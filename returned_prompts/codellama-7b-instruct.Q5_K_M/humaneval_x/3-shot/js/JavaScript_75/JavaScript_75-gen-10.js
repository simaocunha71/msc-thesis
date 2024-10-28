  for (let i = 1; i < 10; i++) {
    if (a % i == 0) {
      if (isPrime(i)) {
        if (isPrime(a / i)) {
          if (isPrime(a / (a / i))) {
            return true;
          }
        }
      }
    }
  }
  return false;
}



