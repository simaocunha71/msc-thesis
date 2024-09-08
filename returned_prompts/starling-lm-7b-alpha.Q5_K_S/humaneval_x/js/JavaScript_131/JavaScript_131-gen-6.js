  let result = 1;
  while (n) {
    if (n % 2) {
      result *= n % 10;
    }
    n = Math.floor(n / 10);
  }
  return result;
}



