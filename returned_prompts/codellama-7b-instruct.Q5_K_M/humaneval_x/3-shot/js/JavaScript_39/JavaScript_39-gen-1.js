  const fibonacci = (n) => {
    if (n <= 1) {
      return n;
    }

    return fibonacci(n - 1) + fibonacci(n - 2);
  }

  const isPrime = (n) => {
    for (let i = 2; i < Math.sqrt(n) + 1; i++) {
      if (n % i == 0) {
        return false;
      }
    }
    return true;
  }

  let result = fibonacci(n);
  while (!isPrime(result)) {
    result = fibonacci(n);
  }
  return result;
}



