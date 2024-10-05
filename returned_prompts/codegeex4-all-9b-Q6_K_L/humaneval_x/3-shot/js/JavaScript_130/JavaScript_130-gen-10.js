  var result = [];
  result[0] = 3;
  result[1] = 2;
  result[2] = 1;
  for (var i = 3; i <= n; i++) {
    if (i % 2 == 0) {
      result[i] = 1 + i / 2;
    } else {
      result[i] = result[i - 1] + result[i - 2] + result[i + 1];
    }
  }
  return result;
}