  var result = 1;

  for (var i = 0; i < n.toString().length; i++) {
    var digit = n % 10;
    if (digit % 2 == 1) {
      result *= digit;
    }
    n = Math.trunc(n / 10);
  }

  return result;
}



