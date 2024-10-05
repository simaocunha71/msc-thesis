  let primes = [];
  
  for(let i = 2; i < n; i++) {
    if(isPrime(i)) {
      primes.push(i);
    }
  }

  return primes;
}

function isPrime(num) {
  for(let i = 2, sqrt = Math.sqrt(num); i <= sqrt; i++)
    if(num % i === 0) return false; 
  return num > 1;
}



