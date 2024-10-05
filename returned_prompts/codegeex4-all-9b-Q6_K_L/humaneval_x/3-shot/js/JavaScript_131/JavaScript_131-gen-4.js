  var product = 1;
  while (n > 0) {
    var digit = n % 10;
    if (digit % 2 == 1) {
      product *= digit;
    }
    n = Math.floor(n / 10);
  }
  return product;
}