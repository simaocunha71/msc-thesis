  if (n == 0) return 0;
  if (n == 1) return 0;
  if (n == 2) return 1;

  var fibfib_0 = 0;
  var fibfib_1 = 0;
  var fibfib_2 = 1;

  for (var i = 3; i <= n; i++) {
    var fibfib_i = fibfib_0 + fibfib_1 + fibfib_2;
    fibfib_0 = fibfib_1;
    fibfib_1 = fibfib_2;
    fibfib_2 = fibfib_i;
  }

  return fibfib_2;
}