  for (let i = n; i >= 2; i--) {
    if (n % i == 0) {
      if (isPrime(i)) {
        return i;
      }
    }
  }
}



