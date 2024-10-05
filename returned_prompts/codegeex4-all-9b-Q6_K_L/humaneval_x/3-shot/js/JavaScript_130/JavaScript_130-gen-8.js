  var result = [3];
  for (let i = 1; i < n + 1; i++) {
    if (i % 2 == 0) {
      result.push(1 + i / 2);
    } else {
      result.push(result[i - 1] + result[i - 2] + result[i - 3]);
    }
  }
  return result;
}