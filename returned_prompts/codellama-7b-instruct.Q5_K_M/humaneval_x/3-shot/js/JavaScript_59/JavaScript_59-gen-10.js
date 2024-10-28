  while (true) {
    for (var i = 2; i < Math.floor(Math.sqrt(n)); i++) {
      if (n % i == 0) {
        n = n / i;
        break;
      }
    }
    if (n == 1) {
      break;
    }
  }
  return n;
}



