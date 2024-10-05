  let max_prime = 2;
  for (const n of lst) {
    if (isPrime(n) && n > max_prime) {
      max_prime = n;
    }
  }

  let sum = 0;
  while (max_prime > 0) {
    sum += max_prime % 10;
    max_prime = Math.floor(max_prime / 10);
  }

  return sum;
}

const isPrime = (n) => {
  if (n <= 1) {
    return false;
  }
  if (n <= 3) {
    return true;
  }
  if (n % 2 == 0 || n % 3 == 0) {
    return false;
  }
  for (let i = 5; i * i <= n; i += 6) {
    if (n % i == 0 || n % (i + 2) == 0) {
      return false;
    }
  }
  return true;
}



