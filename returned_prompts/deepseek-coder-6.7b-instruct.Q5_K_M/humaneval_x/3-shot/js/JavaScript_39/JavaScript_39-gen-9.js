  let fib = [2, 3];
  let i = 2;
  while (fib.length < n) {
    let next = fib[i - 1] + fib[i - 2];
    let isPrime = true;
    for (let j = 2, sqrt = Math.sqrt(next); j <= sqrt; j++)
      if (next % j === 0) {
        isPrime = false;
        break;
      }
    if (isPrime) fib.push(next);
    i++;
  }
  return fib[n - 1];
}



