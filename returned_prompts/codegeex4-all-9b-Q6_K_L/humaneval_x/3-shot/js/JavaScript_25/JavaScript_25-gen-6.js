  var result = [];
  var d = 2;

  while (d <= n) {
    if (n % d == 0) {
      result.push(d);
      n = n / d;
    } else {
      d += 1;
    }
  }

  return result;
}



