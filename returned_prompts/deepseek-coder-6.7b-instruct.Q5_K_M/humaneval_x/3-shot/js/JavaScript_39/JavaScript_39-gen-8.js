  const isPrime = num => {
    for(let i = 2, sqrt = Math.sqrt(num); i <= sqrt; i++)
      if(num % i === 0) return false; 
    return num > 1;
  }

  const fib = (() => {
    let a = 0, b = 1;
    return () => { a = [b, b = a + b][0]; return b };
  })();

  let primeFibNum = 0, i = 2;

  while(n){
    if(isPrime(i)){
      primeFibNum = fib(i);
      n--;
    }
    i++;
  }

  return primeFibNum;
}



