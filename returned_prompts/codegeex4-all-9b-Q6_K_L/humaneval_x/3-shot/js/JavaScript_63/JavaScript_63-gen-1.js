  let fibfib_0 = 0;
  let fibfib_1 = 0;
  let fibfib_2 = 1;

  if (n == 0) {
    return fibfib_0;
  }
  if (n == 1) {
    return fibfib_1;
  }

  for (let i = 2; i <= n; i++) {
    let fibfib_i = fibfib_0 + fibfib_1 + fibfib_2;
    fibfib_0 = fibfib_1;
    fibfib_1 = fibfib_2;
    fibfib_2 = fibfib_i;
  }

  return fibfib_2;
}



