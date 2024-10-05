  const isPrime = (num) => {
    for(let i = 2, sqrt = Math.sqrt(num); i <= sqrt; i++)
      if(num % i === 0) return false; 
    return num > 1;
  }

  const fib = (num) => {
    let a = 1, b = 1; 
    for(let i = 3; i <= num; i++) {
      let temp = b;
      b += a;
      a = temp;
    } 
    return b;
  }

  let i = 1;
  while(n > 0) {
    let fibNum = fib(i);
    if(isPrime(fibNum)) n--;
    i++;
  }

  return fib(i-1);
}



