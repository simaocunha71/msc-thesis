  var result = [n];
  for (let i = 0; i < n - 1; i++) {
    result.push(result[i] + 2 * (i % 2 + 1));
  }
  return result;
}