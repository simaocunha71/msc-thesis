  var result = [];
  for (let i = 1; i <= n; i++) {
    if (i % 2 == 0) {
      result.push(Math.factorial(i));
    } else {
      result.push(i * (i + 1) / 2);
    }
  }
  return result;
}



