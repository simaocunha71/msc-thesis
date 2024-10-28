  let primes = [];
  for (let i = 2; i < n; i++) {
    if (isPrime(i)) {
      primes.push(i);
    }
    if (primes.length === n - 1) {
      break;
    }
  }
  return primes;
}

const isPrime = (num) => {
  if (num < 2) {
    return false;
  }
  for (let i = 2, sqrt = Math.sqrt(num); i <= sqrt; i++) {
    if (num % i === 0) {
      return false;
    }
  }
  return true;
}