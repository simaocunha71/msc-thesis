  const primeFactors = [];
  for (let i = 2; i <= n; i++) {
    if (n % i == 0) {
      primeFactors.push(i);
      n = n / i;
      i--;
    }
  }
  return primeFactors[primeFactors.length - 1];
}