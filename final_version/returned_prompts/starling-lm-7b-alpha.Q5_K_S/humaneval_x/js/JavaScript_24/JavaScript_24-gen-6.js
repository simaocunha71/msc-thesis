  let largest_divisor = -1;
  for (let i = 1; i < n; i++) {
    if (n % i == 0) {
      if (i > largest_divisor) {
        largest_divisor = i;
      }
    }
  }
  return largest_divisor;
}



