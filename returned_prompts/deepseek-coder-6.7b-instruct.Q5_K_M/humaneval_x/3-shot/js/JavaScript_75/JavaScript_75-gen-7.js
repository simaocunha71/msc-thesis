  let factors = [];
  for(let i = 2; i <= a; i++) {
    while(a % i == 0) {
      factors.push(i);
      a = a / i;
    }
  }
  return factors.length == 3 && factors.every(isPrime);
}

function isPrime(n) {
  for(let i = 2, sqrt = Math.sqrt(n); i <= sqrt; i++)
    if(n % i === 0) return false; 
  return n > 1;
}



