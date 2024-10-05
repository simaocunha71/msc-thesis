  var result = [n];
  for (let i = 1; i < n; i++) {
    if (n % 2 == 0) {
      result.push(result[i - 1] + 2);
    } else {
      result.push(result[i - 1] + 2);
    }
  }
  return result;
}

