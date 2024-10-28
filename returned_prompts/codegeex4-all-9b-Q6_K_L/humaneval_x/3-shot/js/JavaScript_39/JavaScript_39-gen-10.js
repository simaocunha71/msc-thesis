  let fib1 = 1, fib2 = 1;
  let result = 2;
  let count = 1;

  while (count < n) {
    let fib3 = fib1 + fib2;
    fib1 = fib2;
    fib2 = fib3;

    if (isPrime(fib3)) {
      result = fib3;
      count += 1;
    }
  }

  return result;
}



