  var result = [1, 3];
  if (n == 0) {
    return result;
  }
  for (var i = 2; i <= n; i++) {
    if (i % 2 == 0) {
      result.push(1 + i / 2);
    } else {
      result.push(result[i - 1] + result[i - 2] + result[i - 3]);
    }
  }
  return result;
}