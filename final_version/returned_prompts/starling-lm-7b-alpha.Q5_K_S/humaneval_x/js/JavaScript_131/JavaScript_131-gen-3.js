  let product = 1;
  while (n > 0) {
    let d = n % 10;
    if (d % 2 != 0) {
      product *= d;
    }
    n = Math.floor(n / 10);
  }
  return product;
}



