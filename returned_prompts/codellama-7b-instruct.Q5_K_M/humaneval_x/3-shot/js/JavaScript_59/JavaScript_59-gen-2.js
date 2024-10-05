  for (let i = n; i >= 2; i--) {
    if (n % i == 0 && isPrime(i)) {
      return i;
    }
  }
}



