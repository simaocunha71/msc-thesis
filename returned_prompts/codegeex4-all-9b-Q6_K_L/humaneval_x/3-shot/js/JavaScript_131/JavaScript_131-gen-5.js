  var product = 1;
  var num = n;
  while (num > 0) {
    var digit = num % 10;
    if (digit % 2 == 1) {
      product *= digit;
    }
    num = Math.floor(num / 10);
  }
  return product;
}