  let result = [];
  for (let i = 1; i <= n; i++) {
    if (i % 2 == 0) {
      result.push(factorial(i));
    } else {
      result.push(sum(i));
    }
  }
  return result;
}

function factorial(n) {
  if (n === 0) {
    return 1;
  }
  return n * factorial(n - 1);
}

function sum(n) {
  if (n === 0) {
    return 0;
  }
  return n + sum(n - 1);
}



