const countUpTo = (n) => {
  const isPrime = (num) => {
    for (let i = 2; i <= Math.sqrt(num); i++) {
      if (num % i === 0) return false;
    }
    return num > 1;
  };
  const primeArray = [];
  for (let i = 2; i < n; i++) {
    if (isPrime(i)) {
      primeArray.push(i);
    }
  }
  return primeArray;
};


