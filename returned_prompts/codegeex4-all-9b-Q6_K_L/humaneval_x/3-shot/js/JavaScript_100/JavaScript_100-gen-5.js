  var result = [n];
  for (var i = 1; i < n; i++) {
    if (n % 2 == 0) {
      result.push(n + 2 * i);
    } else {
      result.push(n + 2 * i - 1);
    }
  }
  return result;
}