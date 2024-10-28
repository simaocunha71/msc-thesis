  var result = [0, 1, 1];
  if (n == 0) {
    return result;
  } else if (n == 1) {
    return [1, 1, 2, 3];
  } else if (n == 2) {
    return [1, 3, 2, 8];
  } else {
    for (let i = 3; i <= n; i++) {
      if (i % 2 == 0) {
        result.push(1 + i / 2);
      } else {
        result.push(result[result.length - 1] + result[result.length - 2] + result[result.length - 3]);
      }
    }
    return result;
  }
}