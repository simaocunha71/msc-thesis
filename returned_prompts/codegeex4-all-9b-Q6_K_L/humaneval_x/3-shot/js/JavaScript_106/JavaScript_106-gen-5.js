  var result = [];
  var factorial = 1;

  for (let i = 1; i <= n; i++) {
    if (i % 2 == 0) {
      factorial *= i;
      result.push(factorial);
    } else {
      var sum = 0;
      for (let j = 1; j <= i; j++) {
        sum += j;
      }
      result.push(sum);
    }
  }

  return result;
}

