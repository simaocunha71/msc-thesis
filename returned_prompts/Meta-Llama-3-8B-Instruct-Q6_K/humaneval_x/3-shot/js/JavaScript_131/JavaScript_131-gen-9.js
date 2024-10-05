  let product = 1;
  while (n > 0) {
    let remainder = n % 10;
    if (remainder % 2 != 0) {
      product *= remainder;
    }
    n = Math.floor(n / 10);
  }
  return product;
}