  let result = [];
  while (n > 1) {
    if (n % 2 != 0) {
      result.push(n);
    }
    if (n % 2 == 0) {
      n = n / 2;
    } else {
      n = 3 * n + 1;
    }
  }
  result.push(1);
  result.sort((a, b) => a - b);
  return result;
}



