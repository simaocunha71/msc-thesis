  let factors = [];
  let divisor = 2;
  while (n > 1) {
    while (n % divisor === 0) {
      n /= divisor;
      factors.push(divisor);
    }
    divisor++;
  }
  return factors;
}
// OR
const factorize = (n) => {
  let factors = [];
  for (let i = 2; i * i <= n; i++) {
    while (n % i === 0) {
      factors.push(i);
      n /= i;
    }
  }
  if (n > 1) {
    factors.push(n);
  }
  return factors;
}