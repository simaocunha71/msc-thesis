  if (n <= 0) {
    throw new Error("Input must be a positive integer");
  }
  if (n === 1) {
    return 1;
  }
  if (n === 2) {
    return 1;
  }
  let a = 1, b = 1, result = 1;
  for (let i = 3; i <= n; i++) {
    result = a + b;
    a = b;
    b = result;
  }
  return result;
}