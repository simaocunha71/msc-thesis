  var result = [];
  for (var i = 1; i <= n; i++) {
    if (i % 2 == 0) {
      result.push(factorial(i));
    } else {
      result.push(sum(i));
    }
  }
  return result;

  function factorial(n) {
    if (n == 0) {
      return 1;
    } else {
      return n * factorial(n - 1);
    }
  }

  function sum(n) {
    var result = 0;
    for (var i = 1; i <= n; i++) {
      result += i;
    }
    return result;
  }
}