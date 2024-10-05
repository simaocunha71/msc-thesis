  const isPrime = (num) => {
    for(let i = 2, sqrt = Math.sqrt(num); i <= sqrt; i++)
      if(num % i === 0) return false; 
    return num > 1;
  }

  let largestPrime = -1;
  for(let i = 0; i < lst.length; i++){
    if(isPrime(lst[i])) largestPrime = Math.max(largestPrime, lst[i]);
  }

  if(largestPrime == -1) return 0;

  return [...largestPrime+''].reduce((a,b)=> a + +b, 0);
}



