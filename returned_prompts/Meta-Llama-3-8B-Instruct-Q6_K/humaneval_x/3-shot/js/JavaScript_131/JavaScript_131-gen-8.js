  let product = 1;
  while (n > 0) {
    let digit = n % 10;
    if (digit % 2 != 0) {
      product *= digit;
    }
    n = Math.floor(n / 10);
  }
  return product;
} 