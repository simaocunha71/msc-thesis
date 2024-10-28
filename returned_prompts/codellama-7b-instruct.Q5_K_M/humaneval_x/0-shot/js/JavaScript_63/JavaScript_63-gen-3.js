const fibfib = (n) => {
  if (n <= 2) {
    return n;
  }
  return fibfib(n - 1) + fibfib(n - 2) + fibfib(n - 3);
};

