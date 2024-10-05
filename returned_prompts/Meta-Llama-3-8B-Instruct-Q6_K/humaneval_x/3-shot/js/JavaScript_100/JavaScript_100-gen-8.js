  var result = [];
  for (let i = 1; i <= n; i++) {
    if (i % 2 == 0) {
      result.push(i * 2 - 1);
    } else {
      result.push(i * 2);
    }
  }
  return result;
}