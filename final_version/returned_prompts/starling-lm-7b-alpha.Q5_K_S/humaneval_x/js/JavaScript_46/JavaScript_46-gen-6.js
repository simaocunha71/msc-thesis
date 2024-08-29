  var result = [0, 0, 2];

  for (var i = 3; i <= n; i++) {
    result[i] = result[i - 1] + result[i - 2] + result[i - 3] + result[i - 4];
  }

  return result[n];
}



