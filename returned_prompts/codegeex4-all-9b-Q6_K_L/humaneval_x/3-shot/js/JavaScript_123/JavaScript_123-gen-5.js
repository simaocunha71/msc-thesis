  var collatz = [n];

  while (n != 1) {
    if (n % 2 == 0) {
      n = n / 2;
    } else {
      n = 3 * n + 1;
    }

    collatz.push(n);
  }

  var result = [];
  for (const num of collatz) {
    if (num % 2 == 1) {
      result.push(num);
    }
  }

  return result.sort(function (a, b) {
    return a - b;
  });
}