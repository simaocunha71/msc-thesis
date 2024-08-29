  const result = [];
  for (let i = 0; i < n; i++) {
    if (i % 2 === 0) {
      result.push(fact(i));
    } else {
      result.push(sum(i));
    }
  }
  return result;
}

function sum(n) {
  let sum = 0;
  for (let i = 1; i <= n; i++) {
    sum += i;
  }
  return sum;
}

function fact(n) {
  let result = 1;
  for (let i = 1; i <= n; i++) {
    result *= i;
  }
  return result;
}



