  var result = 0;
  while (n > 0) {
    var digit = n % 10;
    if (digit % 2 == 1) {
      result *= digit;
    }
    n = Math.floor(n / 10);
  }
  return result;
}



