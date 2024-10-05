  var factor = 2;
  var largest = 1;

  while (factor <= n) {
    if (n % factor == 0) {
      largest = factor;
      n = n / factor;
    } else {
      factor += 1;
    }
  }

  return largest;
}



