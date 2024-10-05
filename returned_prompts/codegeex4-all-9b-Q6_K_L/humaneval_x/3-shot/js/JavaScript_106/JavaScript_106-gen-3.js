  var result = [];
  for (let i = 1; i <= n; i++) {
    if (i % 2 == 0) {
      result.push(factorial(i));
    } else {
      result.push(sumTo(i));
    }
  }
  return result;
}

const factorial = (n) => {
  if (n == 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

const sumTo = (n) => {
  var result = 0;
  for (let i = 1; i <= n; i++) {
    result += i;
  }
  return result;
}