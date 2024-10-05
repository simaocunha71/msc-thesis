  let max_prime = 0;
  for (let i = 2; i * i <= n; i++) {
    if (n % i === 0) {
      let prime = i;
      while (n % prime === 0) {
        n /= prime;
        prime = n % prime === 0 ? n : prime;
      }
      if (prime > max_prime) {
        max_prime = prime;
      }
    }
  }
  return max_prime;
}