  if (n <= 0) {
    return [];
  }
  if (n == 1) {
    return [3];
  }
  if (n == 2) {
    return [1, 3];
  }
  let tribonacciSequence = [1, 3];
  for (let i = 2; i < n; i++) {
    if (i % 2 == 0) {
      tribonacciSequence.push(1 + (i / 2));
    } else {
      let lastTwo = tribonacciSequence[i - 1];
      let lastOne = tribonacciSequence[i - 2];
      let nextOne = tribonacciSequence[i - 3];
      tribonacciSequence.push(lastTwo + lastOne + nextOne);
    }
  }
  return tribonacciSequence;
}