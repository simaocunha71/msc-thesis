  let fib = (m) => {
    let a = 0, b = 1;
    while (m-- > 0) {[a, b] = [b, a + b];}
    return a;
  }

  let isPrime = (num) => {
    for(let i = 2; i < num; i++)
      if(num % i === 0) return false;
    return num > 1;
  }

  let count = 0, i = 1;
  while(count < n) {
    if (isPrime(fib(i))) count++;
    i++;
  }

  return fib(i-1);
}



