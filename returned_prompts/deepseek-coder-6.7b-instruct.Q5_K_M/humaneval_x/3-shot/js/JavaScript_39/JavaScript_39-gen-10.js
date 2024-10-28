  const isPrime = (num) => {
    for(let i = 2, sqrt = Math.sqrt(num); i <= sqrt; i++)
      if(num % i === 0) return false; 
    return num > 1;
  }

  const fib = (n) => {
    let a = 1, b = 1;
    for(let i = 3; i <= n; i++) {
      let c = a + b;
      a = b;
      b = c;
    }
    return b;
  }

  let count = 0;
  let i = 1;

  while(count < n) {
    let f = fib(i);
    if(isPrime(f)) count++;
    i++;
  }

  return fib(i-1);
}



