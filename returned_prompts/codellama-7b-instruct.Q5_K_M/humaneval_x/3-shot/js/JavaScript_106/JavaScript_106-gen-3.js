  var result = [];

  for (let i = 1; i <= n; i++) {
    if (i % 2 == 0) {
      result.push(factorial(i));
    } else {
      result.push(sum(i));
    }
  }

  return result;
}



