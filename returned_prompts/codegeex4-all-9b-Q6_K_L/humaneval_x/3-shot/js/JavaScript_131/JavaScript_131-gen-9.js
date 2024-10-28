  var result = 1;
  var has_odd = false;
  while (n > 0) {
    var d = n % 10;
    if (d % 2 == 1) {
      result *= d;
      has_odd = true;
    }
    n = Math.floor(n / 10);
  }
  return has_odd ? result : 0;
}