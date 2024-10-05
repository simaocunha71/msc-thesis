  if (n == 0 || n == 1) {
    return 0;
  }
  if (n == 2) {
    return 1;
  }
  var fibfib1 = 0;
  var fibfib2 = 0;
  var fibfib3 = 1;
  var result = 1;
  for (let i = 3; i <= n; i++) {
    result = fibfib1 + fibfib2 + fibfib3;
    fibfib1 = fibfib2;
    fibfib2 = fibfib3;
    fibfib3 = result;
  }
  return result;
}