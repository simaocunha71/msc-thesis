/*
  I'm going to use the Fibonacci sequence to solve this problem.
  */
  let fibArray = [0, 0, 1];
  const fib = (n) => {
    if (n == 0 || n == 1) return 0;
    if (n == 2) return 1;
    if (fibArray[n]) return fibArray[n];
    let result = fib(n - 1) + fib(n - 2) + fib(n - 3);
    fibArray[n] = result;
    return result;
  };
  return fib(n);

