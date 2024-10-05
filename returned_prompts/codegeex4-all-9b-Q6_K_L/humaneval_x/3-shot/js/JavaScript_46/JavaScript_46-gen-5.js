  var result = [0, 0, 2, 0];
  while (result.length <= n) {
    result.push(result[result.length - 1] + result[result.length - 2] + result[result.length - 3] + result[result.length - 4]);
  }
  return result[n];
}

