  const isPrime = (num) => {
    if (num < 2) {
      return false;
    }
    for (let i = 2; i < num; i++) {
      if (num % i == 0) {
        return false;
      }
    }
    return true;
  }

  const fib = (n) => {
    if (n == 0) {
      return 0;
    } else if (n == 1) {
      return 1;
    } else {
      return fib(n - 1) + fib(n - 2);
    }
  }

  let count = 0;
  let current = 0;
  while (true) {
    current = fib(current);
    if (isPrime(current)) {
      count += 1;
    }
    if (count == n) {
      return current;
    }
  }
}