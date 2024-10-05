  var factor = 2;

  while (n > 1) {
    if (n % factor == 0) {
      n = n / factor;
    } else {
      factor += 1;
    }
  }

  return factor;
}