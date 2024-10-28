  if (n < 3) {
    return 0;
  }
  if (n == 3) {
    return 1;
  }

  var result = 0;
  var fibfib_1 = 1;
  var fibfib_2 = 0;
  var fibfib_3 = 0;

  for (let i = 3; i <= n; i++) {
    result = fibfib_1 + fibfib_2 + fibfib_3;
    fibfib_3 = fibfib_2;
    fibfib_2 = fibfib_1;
    fibfib_1 = result;
  }

  return result;
}