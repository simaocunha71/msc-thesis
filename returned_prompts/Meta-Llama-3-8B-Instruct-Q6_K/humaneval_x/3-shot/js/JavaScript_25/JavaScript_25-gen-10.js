  let factors = [];
  let divisor = 2;
  while (n > 1) {
    if (n % divisor == 0) {
      let count = 0;
      while (n % divisor == 0) {
        n = Math.floor(n / divisor);
        count++;
      }
      factors.push.apply(factors, Array(count + 1).fill(divisor));
    }
    divisor++;
  }
  return factors;
}