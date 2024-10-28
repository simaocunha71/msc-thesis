  if (n == 0) {
    return [1];
  } else if (n == 1) {
    return [1, 3];
  } else if (n == 2) {
    return [1, 3, 2];
  } else {
    var result = [1, 3, 2];
    for (let i = 3; i <= n; i++) {
      if (i % 2 == 0) {
        result.push(1 + i / 2);
      } else {
        result.push(result[i - 1] + result[i - 2] + result[i - 3]);
      }
    }
    return result;
  }
}