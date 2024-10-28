  var result = [0, 0, 2, 0];

  if (n < 4) {
    return result[n];
  }

  for (let i = 4; i <= n; i++) {
    result.push(result[i - 1] + result[i - 2] + result[i - 3] + result[i - 4]);
  }

  return result[n];
}



