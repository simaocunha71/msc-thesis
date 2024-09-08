  let result = 0;
  let binary = '';

  while (N > 0) {
    result += N % 2;
    binary = (N % 2) + binary;
    N = Math.floor(N / 2);
  }

  return result + '';
}



