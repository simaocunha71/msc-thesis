  const isPrime = (num) => {
    for (let i = 2; i <= Math.sqrt(num); i++) {
      if (num % i === 0) {
        return false;
      }
    }
    return num > 1;
  };

  let fib1 = 0;
  let fib2 = 1;
  let count = 0;

  while (true) {
    let fib = fib1 + fib2;
    fib1 = fib2;
    fib2 = fib;

    if (isPrime(fib)) {
      count++;
      if (count === n) {
        return fib;
      }
    }
  }
}



