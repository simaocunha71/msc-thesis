  let result = 1;
  for (let i = n; i >= 1; i--) {
    result *= factorial(i);
  }
  return result;
}

const factorial = (n) => {
  let result = 1;
  for (let i = 2; i <= n; i++) {
    result *= i;
  }
  return result;
}



