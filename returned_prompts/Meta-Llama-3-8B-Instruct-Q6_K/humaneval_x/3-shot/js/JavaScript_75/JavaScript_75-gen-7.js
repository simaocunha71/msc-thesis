  for (let i = 2; i <= Math.sqrt(a); i++) {
    if (isPrime(i)) {
      for (let j = i; j <= Math.sqrt(a); j++) {
        if (isPrime(j) && a % (i * j) == 0) {
          for (let k = j; k <= Math.sqrt(a); k++) {
            if (isPrime(k) && a % (i * j * k) == 0) {
              return true;
            }
          }
        }
      }
    }
  }
  return false;

  function isPrime(num) {
    if (num <= 1) {
      return false;
    }
    for (let i = 2; i <= Math.sqrt(num); i++) {
      if (num % i == 0) {
        return false;
      }
    }
    return true;
  }
}