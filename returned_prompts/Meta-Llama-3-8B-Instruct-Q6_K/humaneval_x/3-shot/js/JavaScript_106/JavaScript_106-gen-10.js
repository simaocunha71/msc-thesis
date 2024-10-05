  let result = [];
  for (let i = 0; i < n; i++) {
    if (i % 2 === 0) {
      result.push(factorial(i));
    } else {
      let sum = 0;
      for (let j = 1; j <= i; j++) {
        sum += j;
      }
      result.push(sum);
    }
  }
  return result;
}

function factorial(n) {
  let result = 1;
  for (let i = 2; i <= n; i++) {
    result *= i;
  }
  return result;
}