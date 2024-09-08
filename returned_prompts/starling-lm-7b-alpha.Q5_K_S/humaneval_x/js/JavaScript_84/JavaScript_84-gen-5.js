  let result = '';
  let sum = 0;
  while (N > 0) {
    sum += (N % 2);
    N = Math.floor(N / 2);
  }
  while (sum > 0) {
    result += (sum % 2);
    sum = Math.floor(sum / 2);
  }
  return result;
}



