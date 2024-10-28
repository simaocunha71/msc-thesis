  let primes = [];
  for  (let i = ２; i < n; i++) {
    let isPrime = true;
    for  (let j = ２; j * j <= i; j++) {
      if  (i % j === 0) {
        isPrime = false;
        break;
      }
    }
    if  (isPrime) {
      primes.push(i);
    }
  }
  return primes;
}



