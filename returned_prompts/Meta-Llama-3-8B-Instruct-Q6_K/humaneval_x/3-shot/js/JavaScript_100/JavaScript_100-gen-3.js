  var result = [];
  var i = 1;
  while (n > 0) {
    if (n % 2 == 1) {
      result.push(i);
      i += 2;
    } else {
      result.push(i);
      i += 1;
    }
    n -= 1;
  }
  return result;
}