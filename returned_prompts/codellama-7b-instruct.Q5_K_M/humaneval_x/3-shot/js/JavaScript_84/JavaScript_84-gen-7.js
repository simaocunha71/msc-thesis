  var result = 0;
  while (N > 0) {
    result += N % 2;
    N = Math.floor(N / 2);
  }
  return result.toString(2);
}



