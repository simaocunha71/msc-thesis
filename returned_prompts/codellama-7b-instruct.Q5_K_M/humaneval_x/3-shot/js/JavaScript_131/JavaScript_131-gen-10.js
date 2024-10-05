  var result = 1;

  while (n > 0) {
    var last_digit = n % 10;
    if (last_digit % 2 == 1) {
      result *= last_digit;
    }
    n = Math.floor(n / 10);
  }

  return result;
}



