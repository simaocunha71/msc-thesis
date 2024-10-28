  if (n == 0) {
    return 0;
  }

  if (n == 1) {
    return 0;
  }

  if (n == 2) {
    return 2;
  }

  if (n == 3) {
    return 0;
  }

  var first = 0;
  var second = 0;
  var third = 2;
  var fourth = 0;

  for (var i = 4; i <= n; i++) {
    fourth = first + second + third;
    first = second;
    second = third;
    third = fourth;
  }

  return fourth;
}



