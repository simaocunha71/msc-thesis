  var a = 0;
  var b = 0;
  var c = 1;
  var result = 0;

  if (n == 0) {
    return 0;
  } else if (n == 1) {
    return 0;
  } else if (n == 2) {
    return 1;
  } else {
    for (var i = 3; i <= n; i++) {
      result = a + b + c;
      a = b;
      b = c;
      c = result;
    }
  }

  return result;
}