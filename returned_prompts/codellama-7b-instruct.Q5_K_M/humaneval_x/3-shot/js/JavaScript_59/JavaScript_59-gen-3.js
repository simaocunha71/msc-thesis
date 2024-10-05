  for (let i = n; i > 1; i--) {
    if (n % i == 0) {
      if (isPrime(i)) {
        return i;
      }
    }
  }
  return 1;
}



