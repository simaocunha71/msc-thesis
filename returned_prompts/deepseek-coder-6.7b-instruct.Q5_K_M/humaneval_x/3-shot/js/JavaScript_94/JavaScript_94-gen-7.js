  const isPrime = n => {
    for(let i = 2, sqrt = Math.sqrt(n); i <= sqrt; i++)
      if(n % i === 0) return false; 
    return n > 1;
  }

  let prime = lst.filter(isPrime);
  let maxPrime = Math.max(...prime);
  let sumDigits = maxPrime.toString().split('').reduce((a, b) => Number(a) + Number(b), 0);

  return sumDigits;
}



