  const isPrime = (n) => {
    if (n < 2) {
      return false;
    }
    for (let i = 2; i <= Math.sqrt(n); i++) {
      if (n % i == 0) {
        return false;
      }
    }
    return true;
  }

  let largest_prime = -1;
  for (const n of lst) {
    if (isPrime(n) && n > largest_prime) {
      largest_prime = n;
    }
  }

  if (largest_prime == -1) {
    return 0;
  }

  let sum = 0;
  while (largest_prime > 0) {
    sum += largest_prime % 10;
    largest_prime = Math.floor(largest_prime / 10);
  }
  return sum;
}