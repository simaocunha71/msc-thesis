  const isPrime = (num) => {
    for(let i = 2, sqrt = Math.sqrt(num); i <= sqrt; i++)
      if(num % i === 0) return false; 
    return num > 1;
  }

  let maxPrime = -1;
  for(let i = 0; i < lst.length; i++){
    if(isPrime(lst[i])){
      maxPrime = Math.max(maxPrime, lst[i]);
    }
  }

  return maxPrime === -1 ? null :
    maxPrime.toString().split('').reduce((a, b) => Number(a) + Number(b), 0);
}



