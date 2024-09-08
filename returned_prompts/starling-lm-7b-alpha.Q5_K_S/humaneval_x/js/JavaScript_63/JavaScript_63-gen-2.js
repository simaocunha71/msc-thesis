  if (n == 0 || n == 1) {
    return 0;
  } else if (n == 2) {
    return 1;
  } else {
    const fib_n_minus_1 = fibfib(n - 1);
    const fib_n_minus_2 = fibfib(n - 2);
    const fib_n_minus_3 = fibfib(n - 3);
    return fib_n_minus_1 + fib_n_minus_2 + fib_n_minus_3;
  }
}



