  var result = [];
  if (n <= 0) {
    return result;
  }
  result.push(3);
  if (n <= 1) {
    return result;
  }
  result.push(1);
  if (n <= 2) {
    return result;
  }
  result.push(2);
  if (n <= 3) {
    return result;
  }
  result.push(8);
  for (let i = 4; i <= n; i++) {
    let value = result[i - 1] + result[i - 2] + result[i - 3];
    result.push(value);
  }
  return result;
}