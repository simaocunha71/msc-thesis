  let product = 1;
  while (n > 0) {
    const d = n % 10;
    if (d % 2 !== 0) {
      product *= d;
    }
    n = (n - d) / 10 | 0;
  }
  return product;
}



