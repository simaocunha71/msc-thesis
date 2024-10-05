  let i = 2;
  let largest_factor = 1;

  while (i * i <= n) {
    if (n % i) {
      i++;
    } else {
      n /= i;
      largest_factor = i;
    }
  }

  if (n > 1) {
    largest_factor = n;
  }

  return largest_factor;
}