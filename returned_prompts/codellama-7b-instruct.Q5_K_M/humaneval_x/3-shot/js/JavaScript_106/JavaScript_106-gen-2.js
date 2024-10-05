  var result = [];
  for (var i = 1; i <= n; i++) {
    if (i % 2 == 0) {
      result.push(factorial(i));
    } else {
      result.push(sumFrom1To(i));
    }
  }
  return result;
}



