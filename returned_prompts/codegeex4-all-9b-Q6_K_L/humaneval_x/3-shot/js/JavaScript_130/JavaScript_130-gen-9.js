  var result = [1, 3];

  for (let i = 2; i <= n; i++) {
    if (i % 2 == 0) {
      result.push(1 + i / 2);
    } else {
      result.push(result[i - 1] + result[i - 2] + result[i + 1]);
    }
  }

  return result;
}