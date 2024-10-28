  let sum = 0;
  let binary = '';
  while (N > 0) {
    let remainder = N % 2;
    binary += remainder.toString();
    sum += remainder;
    N = Math.floor(N / 2);
  }
  return binary;
}