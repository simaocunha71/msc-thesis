  var result = 1;

  while (n > 0) {
    if (n % 2 == 1) {
      result *= n % 10;
    }
    n = Math.floor(n / 10);
  }

  return result;
}



