  let max_factor = 1;
  for (let i = 2; i <= Math.sqrt(n); i++) {
    while (n % i === 0) {
      max_factor = i;
      n /= i;
    }
  }
  return max_factor;
}



