const fibfib = (n) => {
  // Base case
  if (n <= 2) {
    return n - 1;
  }
  // Recursive case
  else {
    return fibfib(n - 1) + fibfib(n - 2) + fibfib(n - 3);
  }
}

