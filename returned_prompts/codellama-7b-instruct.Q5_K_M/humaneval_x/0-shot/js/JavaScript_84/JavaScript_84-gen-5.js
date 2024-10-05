  const digits = new Set();
  let sum = 0;
  let binary = 0;
  
  while (N > 0) {
    binary = N % 2;
    N = (N - binary) / 2;
    sum += binary;
    digits.add(binary);
  }
  
  return sum;
}
