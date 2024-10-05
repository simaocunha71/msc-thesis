  var result = 1;
  var is_odd = true;

  while (n > 0) {
    var digit = n % 10;
    if (digit % 2 == 0) {
      is_odd = false;
    } else {
      result *= digit;
    }
    n = Math.floor(n / 10);
  }

  if (is_odd) {
    return result;
  } else {
    return 0;
  }
}