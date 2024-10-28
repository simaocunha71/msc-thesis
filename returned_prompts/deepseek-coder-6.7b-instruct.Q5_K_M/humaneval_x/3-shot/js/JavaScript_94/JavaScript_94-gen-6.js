  let isPrime = num => {
    for(let i = 2, sqrt = Math.sqrt(num); i <= sqrt; i++)
      if(num % i === 0) return false; 
    return num > 1;
  }

  let maxPrime = Math.max(...lst.filter(isPrime));
  return String(maxPrime).split('').reduce((a, b) => a + +b, 0);
}



