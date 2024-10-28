  let fib = [0, 1];
  let prime = [];
  let i = 0;
  let j = 0;

  while (prime.length < n) {
    fib[i] = fib[j] + fib[j + 1];
    if (isPrime(fib[i])) prime.push(fib[i]);
    i = (i + 1) % 2;
    j = (j + 1) % 2;
  }

  return prime[n - 1];
}

const isPrime = (num) => {
  if (num < 2) return false;
  for (let i = 2, sqrt = Math.sqrt(num); i <= sqrt; i++)
    if (num % i === 0) return false;
  return true;
}



