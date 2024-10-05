  var result = [n];
  if (n == 1) {
    return result;
  }
  while (n != 1) {
    n = n % 2 == 0 ? n + 1 : n + 2;
    result.push(n);
  }
  return result;
}



