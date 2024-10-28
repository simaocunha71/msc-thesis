  var result = [];
  result.push(n);

  while (n > 0) {
    if (n % 2 == 1) {
      n = n + 1;
    } else {
      n = n + 2;
    }
    result.push(n);
  }

  return result;
}



