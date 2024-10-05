  let primes = [2];
  let fibs = [0, 1];
  let i = 3;

  while(primes.length < n){
    if(isPrime(i) && isFib(i)){
      primes.push(i);
    }
    i++;
  }

  return primes[n-1];

  function isFib(num){
    while(fibs[fibs.length - 1] < num){
      fibs.push(fibs[fibs.length - 1] + fibs[fibs.length - 2]);
    }
    return fibs.includes(num);
  }

  function isPrime(num){
    for(let i = 2, sqrt = Math.sqrt(num); i <= sqrt; i++)
      if(num % i === 0) return false;
    return num > 1;
  }
}



