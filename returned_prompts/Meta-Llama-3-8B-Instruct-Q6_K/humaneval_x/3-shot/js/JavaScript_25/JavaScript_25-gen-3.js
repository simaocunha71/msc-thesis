  let factors = [];
  let i = 2;
  while (i * i <= n) {
    let count = 0;
    while (n % i == 0) {
      n /= i;
      count++;
    }
    if (count > 0) {
      factors.push(i);
      for (let j = 1; j <= count; j++) {
        factors.push(i);
      }
    }
    i++;
  }
  if (n > 1) {
    factors.push(n);
  }
  return factors;
}