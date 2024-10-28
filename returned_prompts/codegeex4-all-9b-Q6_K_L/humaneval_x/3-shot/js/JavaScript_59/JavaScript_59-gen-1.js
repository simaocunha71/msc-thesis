  let largest_factor = 2;
  while (n % 2 == 0) {
    n = Math.floor(n / 2);
    largest_factor = 2;
  }
  for (let i = 3; i <= Math.sqrt(n); i += 2) {
    while (n % i == 0) {
      n = Math.floor(n / i);
      largest_factor = i;
    }
  }
  if (n > 2) {
    largest_factor = n;
  }
  return largest_factor;
}