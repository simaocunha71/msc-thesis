  for (let i = 2; i * i <= n; i++) {
    if (n % i === 0) {
      while (n % i === 0) {
        n /= i;
      }
      return i;
    }
  }
  return n;
}



