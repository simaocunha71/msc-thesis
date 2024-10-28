  const result = [];
  for (let i = 2; i < n; i++) {
    if (isPrime(i)) {
      result.push(i);
    }
  }
  return result;

  function isPrime(num) {
    if (num <= 1) return false;
    for (let i = 2, sqrt = Math.sqrt(num); i <= sqrt; i++) {
      if (num % i === 0) return false;
    }
    return true;
  }
}:



