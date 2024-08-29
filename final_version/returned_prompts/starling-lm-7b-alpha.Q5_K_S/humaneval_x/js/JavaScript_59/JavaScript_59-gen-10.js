  let largestFactor = 1;
  for (let i = 2; i <= n; i++) {
    while (n % i === 0) {
      if (isPrime(i)) {
        largestFactor = i;
      }
      n /= i;
    }
  }
  return largestFactor;
}



