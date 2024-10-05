  let fib = (m) => {
    if (m < 2) {
      return m;
    } else {
      return fib(m - 1) + fib(m - 2);
    }
  };

  let isPrime = (num) => {
    for(let i = 2; i < num; i++)
      if(num % i === 0) return false;
    return num > 1;
  };

  let count = 0;
  let i = 0;

  while(count < n) {
    i++;
    if (isPrime(fib(i))) count++;
  }

  return fib(i);
}


