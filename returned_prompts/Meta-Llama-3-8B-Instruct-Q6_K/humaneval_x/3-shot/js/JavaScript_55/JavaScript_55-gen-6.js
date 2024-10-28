  if (n <= 0) {
    throw new Error('n must be a positive integer');
  }
  if (n == 1) {
    return 1;
  }
  let a = 1;
  let b = 1;
  for (let i = 2; i < n; i++) {
    let temp = a + b;
    a = b;
    b = temp;
  }
  return b;
}