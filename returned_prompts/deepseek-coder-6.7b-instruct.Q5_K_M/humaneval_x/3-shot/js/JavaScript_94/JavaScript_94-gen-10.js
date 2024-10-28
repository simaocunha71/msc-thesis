  const isPrime = n => {
    for(let i = 2, sqrt = Math.sqrt(n); i <= sqrt; i++)
      if(n % i === 0) return false; 
    return n > 1;
  }

  let maxPrime = -1;
  for(let i = 0; i < lst.length; i++){
    if(isPrime(lst[i])){
      maxPrime = Math.max(maxPrime, lst[i]);
    }
  }

  return maxPrime.toString().split('').reduce((a, b) => a + +b, 0);
}



