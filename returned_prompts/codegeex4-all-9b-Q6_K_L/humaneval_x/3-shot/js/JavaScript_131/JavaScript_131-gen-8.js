  var product = 1;
  var isOdd = false;

  while (n > 0) {
    var digit = n % 10;
    if (digit % 2 == 1) {
      product *= digit;
      isOdd = true;
    }
    n = Math.floor(n / 10);
  }

  return isOdd ? product : 0;
}



