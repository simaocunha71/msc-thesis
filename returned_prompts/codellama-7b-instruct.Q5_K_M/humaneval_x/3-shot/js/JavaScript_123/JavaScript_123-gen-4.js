  var result = [];

  if (n == 1) {
    return [1];
  }

  while (n > 1) {
    if (n % 2 == 0) {
      n /= 2;
    } else {
      n = 3 * n + 1;
    }
    result.push(n);
  }

  return result;
}



