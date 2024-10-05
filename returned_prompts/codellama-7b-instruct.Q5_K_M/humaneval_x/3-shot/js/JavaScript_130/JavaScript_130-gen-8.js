  var result = [1, 3];
  if (n < 2) {
    return result;
  }

  var i = 2;
  var current = 0;
  while (i <= n) {
    current = result[result.length - 1] + result[result.length - 2] + result[result.length - 3];
    result.push(current);
    i += 1;
  }

  return result;
}



