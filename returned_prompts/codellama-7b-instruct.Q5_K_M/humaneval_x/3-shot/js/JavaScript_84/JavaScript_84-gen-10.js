  var result = '';
  while (N > 0) {
    result = result + (N % 2).toString();
    N = Math.floor(N / 2);
  }
  return result;
}



