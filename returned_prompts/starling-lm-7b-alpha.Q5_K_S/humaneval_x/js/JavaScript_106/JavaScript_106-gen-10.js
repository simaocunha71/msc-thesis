  let result = [];

  for (let i = 0; i < n; i++) {
    if (i % 2 === 0) {
      result.push(factorial(i));
    } else {
      result.push(sum(i));
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

function sum(n) {
  let result = 0;
  for (let i = 1; i <= n; i++) {
    result += i;
  }
  return result;
}



