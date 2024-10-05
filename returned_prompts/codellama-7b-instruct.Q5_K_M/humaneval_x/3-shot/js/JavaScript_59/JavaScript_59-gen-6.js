  if (isPrime(n)) {
    return n;
  }
  else {
    for (let i = n; i > 1; i--) {
      if (n % i == 0 && isPrime(i)) {
        return i;
      }
    }
  }
}



