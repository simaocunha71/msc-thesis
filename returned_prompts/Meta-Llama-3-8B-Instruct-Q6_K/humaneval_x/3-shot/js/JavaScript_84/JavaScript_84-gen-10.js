  let sum = 0, binary = '';
  while(N > 0) {
    let remainder = N % 2;
    binary = remainder + binary;
    sum += remainder;
    N = Math.floor(N / 2);
  }
  return binary;
}