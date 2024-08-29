  let result = 0;

  for (let i = 2; i <= n / 2; i++) {
    while (n % i == 0) {
      if (isPrime(i)) {
        result = i;
      }
      n /= i;
    }
  }

  if (n > 2 && isPrime(n)) {
    result = n;
  }

  return result;
}



