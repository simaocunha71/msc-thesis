  if (n <= 0) {
    throw new Error('n must be a positive integer');
  }
  if (n == 1) {
    return 1;
  }
  let a = 1, b = 1, result = 1;
  for (let i = 2; i < n; i++) {
    result = a + b;
    a = b;
    b = result;
  }
  return result;
}