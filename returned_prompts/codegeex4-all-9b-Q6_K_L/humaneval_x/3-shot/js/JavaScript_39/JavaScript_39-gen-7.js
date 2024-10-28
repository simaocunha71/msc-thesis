  const isPrime = (num) => {
    for (let i = 2; i <= Math.sqrt(num); i++) {
      if (num % i === 0) {
        return false;
      }
    }
    return num > 1;
  };

  let count = 0;
  let fib1 = 1;
  let fib2 = 1;
  let fib3;

  while (count < n) {
    fib3 = fib1 + fib2;
    if (isPrime(fib3)) {
      count += 1;
    }
    fib1 = fib2;
    fib2 = fib3;
  }

  return fib3;
}