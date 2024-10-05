  var result = [];

  while (n > 0) {
    result.push(n);
    n = (n % 2 == 0) ? n + 1 : n + 2;
  }

  return result;
}



