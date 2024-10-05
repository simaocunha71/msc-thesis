  var i = 2;
  while (n > i) {
    if (n % i == 0) {
      n = n / i;
    } else {
      i = i + 1;
    }
  }
  return i;
}



