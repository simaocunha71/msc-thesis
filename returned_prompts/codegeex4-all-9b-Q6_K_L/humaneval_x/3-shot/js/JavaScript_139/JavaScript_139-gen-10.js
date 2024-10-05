  let result = 1;
  let current_factorial = 1;

  for (let i = 1; i <= n; i++) {
    current_factorial *= i;
    result *= current_factorial;
  }

  return result;
}