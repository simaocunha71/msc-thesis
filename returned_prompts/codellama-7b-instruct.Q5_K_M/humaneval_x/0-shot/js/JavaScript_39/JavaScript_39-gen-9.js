  const fib = (n) => {
    if (n === 1) return 1;
    if (n === 2) return 1;
    return fib(n-1) + fib(n-2);
  };

  const isPrime = (n) => {
    if (n === 1) return false;
    if (n === 2) return true;
    for (let i = 2; i <= Math.sqrt(n); i += 1) {
      if (n % i === 0) return false;
    }
    return true;
  };

  let result = 0;
  while (!isPrime(result)) result = fib(n);
  return result;
};

